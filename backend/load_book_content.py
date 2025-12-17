"""
Script to load all book content into the Qdrant vector database
"""
import os
import sys
from pathlib import Path
import re
import hashlib

# Add the current directory to the path so we can import the main app components
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import model, qdrant_client, collection_name, PointStruct
from qdrant_client.http import models
import uuid
from time import time

def extract_text_from_md_content(content):
    """
    Extract clean text from markdown content, removing frontmatter and markdown syntax
    """
    # Remove frontmatter (content between --- markers)
    lines = content.split('\n')
    frontmatter_removed = []
    in_frontmatter = False

    for line in lines:
        if line.strip().startswith('---'):
            in_frontmatter = not in_frontmatter
            continue
        if not in_frontmatter:
            frontmatter_removed.append(line)

    clean_content = '\n'.join(frontmatter_removed)

    # Remove markdown syntax but keep the text content
    # Remove headers
    clean_content = re.sub(r'^#+\s+', '', clean_content, flags=re.MULTILINE)
    # Remove bold/italic
    clean_content = re.sub(r'\*{1,2}(.*?)\*{1,2}', r'\1', clean_content)
    # Remove code blocks with language specifier
    clean_content = re.sub(r'```.*?\n(.*?)```', '', clean_content, flags=re.DOTALL)
    # Remove inline code
    clean_content = re.sub(r'`(.*?)`', r'\1', clean_content)
    # Remove links [text](url) -> text
    clean_content = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_content)
    # Remove image syntax ![alt](url) -> alt
    clean_content = re.sub(r'!\[(.*?)\]\(.*?\)', r'\1', clean_content)
    # Remove emphasis markers like quotes, lists, etc.
    clean_content = re.sub(r'^>\s+', '', clean_content, flags=re.MULTILINE)
    clean_content = re.sub(r'^-\s+', '', clean_content, flags=re.MULTILINE)
    clean_content = re.sub(r'^\d+\.\s+', '', clean_content, flags=re.MULTILINE)

    # Clean up extra whitespace
    clean_content = re.sub(r'\n\s*\n', '\n\n', clean_content)  # Remove excessive blank lines
    clean_content = clean_content.strip()

    return clean_content

def load_documents_to_qdrant():
    """
    Load all markdown files from the book docs directory into Qdrant
    """
    print("Starting to load book content into Qdrant...")

    # Get the book docs directory (assuming it's in the parent directory of backend)
    book_docs_dir = Path("../book/docs")

    if not book_docs_dir.exists():
        print(f"Book docs directory not found: {book_docs_dir}")
        # Try alternative path
        book_docs_dir = Path("../../book/docs")
        if not book_docs_dir.exists():
            print(f"Book docs directory not found in alternative path either: {book_docs_dir}")
            return

    md_files = list(book_docs_dir.rglob("*.md")) + list(book_docs_dir.rglob("*.mdx"))

    print(f"Found {len(md_files)} markdown files to process")

    total_chunks_added = 0

    for file_path in md_files:
        print(f"Processing file: {file_path}")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract clean text from markdown
            clean_text = extract_text_from_md_content(content)

            if not clean_text.strip():
                print(f"  Skipping {file_path} - no content after processing")
                continue

            # Create chunks from the content (split by paragraphs)
            paragraphs = [p.strip() for p in clean_text.split('\n\n') if p.strip()]

            # Further split large paragraphs if needed
            chunks = []
            for para in paragraphs:
                if len(para) > 1000:  # If paragraph is too long, split by sentences
                    sentences = re.split(r'[.!?]+\s+', para)
                    current_chunk = ""
                    for sentence in sentences:
                        if len(current_chunk + " " + sentence) < 500:
                            current_chunk += " " + sentence if current_chunk else sentence
                        else:
                            if current_chunk:
                                chunks.append(current_chunk.strip())
                            current_chunk = sentence
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                else:
                    chunks.append(para)

            # Filter out short chunks
            chunks = [chunk for chunk in chunks if len(chunk) > 50]

            if not chunks:
                print(f"  No valid chunks found in {file_path}")
                continue

            print(f"  Split into {len(chunks)} chunks")

            # Process each chunk
            points = []
            for i, chunk in enumerate(chunks):
                # Generate embedding for the chunk
                embedding = model.encode(chunk)

                # Create a unique ID for this chunk using a hash of the content
                content_hash = hashlib.md5(chunk.encode()).hexdigest()
                point_id = f"{content_hash}_{i}"

                # Create the point for Qdrant
                point = PointStruct(
                    id=point_id,
                    vector=embedding.tolist(),  # Convert numpy array to list
                    payload={
                        "text": chunk,
                        "source_file": str(file_path.relative_to(book_docs_dir)),
                        "chunk_index": i,
                        "title": file_path.stem  # Use the filename without extension as title
                    }
                )
                points.append(point)

            # Upload points to Qdrant
            if points:
                qdrant_client.upsert(
                    collection_name=collection_name,
                    points=points
                )

                total_chunks_added += len(points)
                print(f"  Added {len(points)} chunks to Qdrant from {file_path}")
            else:
                print(f"  No points created for {file_path}")

        except Exception as e:
            print(f"  Error processing {file_path}: {str(e)}")
            continue

    print(f"\nSuccessfully loaded {total_chunks_added} chunks from book content into Qdrant!")
    print(f"All content is now available for RAG-based chat functionality.")

if __name__ == "__main__":
    load_documents_to_qdrant()