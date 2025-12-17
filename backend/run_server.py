"""
Script to run the backend server with optional content loading
"""
import subprocess
import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run the backend server')
    parser.add_argument('--load-content', action='store_true',
                       help='Load book content to Qdrant before starting server')
    parser.add_argument('--port', type=int, default=8001,
                       help='Port to run the server on (default: 8001)')

    args = parser.parse_args()

    if args.load_content:
        print("Loading book content to Qdrant...")

        # Import and run the content loader
        from load_book_content import load_documents_to_qdrant
        load_documents_to_qdrant()

        print("\nContent loading completed!")

    print(f"\nStarting backend server on port {args.port}...")

    # Run the main server
    import uvicorn
    import main
    uvicorn.run(main.app, host="0.0.0.0", port=args.port)

if __name__ == "__main__":
    main()