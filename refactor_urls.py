import os
import re

def replace_localhost():
    src_dir = os.path.join("d:\\", "2026 websites", "Financial_Advisor-main", "src")
    
    # Pattern to match 'http://localhost:5000/something' or "http://localhost:5000/something" or `http://localhost:5000/something`
    # We want to replace 'http://localhost:5000' with ${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'}
    # So 'http://localhost:5000/api' becomes `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'}/api`
    
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.jsx') or file.endswith('.js'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # We can replace 'http://localhost:5000 with `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'}`
                # We need to make sure the string is a template literal if it isn't already.
                
                # For basic strings: 'http://localhost:5000/path' -> `${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'}/path`
                # Let's do a regex replacement.
                
                new_content = re.sub(
                    r"['\"]http://localhost:5000([^'\"]*)['\"]",
                    r"`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'}\1`",
                    content
                )
                
                # Also handle if it's already in backticks: `http://localhost:5000/path/${id}`
                new_content = re.sub(
                    r"`http://localhost:5000([^`]*)`",
                    r"`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000'}\1`",
                    new_content
                )

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")

if __name__ == '__main__':
    replace_localhost()
