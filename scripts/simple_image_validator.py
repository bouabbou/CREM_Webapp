#!/usr/bin/env python3
"""
Simple Image Path Validator
Validates all image references without Django dependencies
"""

import os
import re
from pathlib import Path

class SimpleImageValidator:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.static_dir = self.base_dir / 'static'
        self.templates_dir = self.base_dir / 'templates'
        self.broken_links = []
        self.valid_links = []
        
    def validate_static_path(self, static_path):
        """Validate a static file path exists"""
        try:
            # Remove leading static/ if present
            if static_path.startswith('static/'):
                static_path = static_path[7:]
            
            # Handle relative paths starting with ../
            if static_path.startswith('../'):
                # Count how many levels up we need to go
                up_levels = static_path.count('../')
                remaining_path = static_path.replace('../', '', up_levels)
                full_path = self.base_dir
                for _ in range(up_levels):
                    full_path = full_path.parent
                full_path = full_path / remaining_path
            else:
                full_path = self.static_dir / static_path
            
            return full_path.exists()
        except:
            return False
    
    def extract_image_paths_from_file(self, file_path, pattern):
        """Extract image paths from a file using regex pattern"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            matches = re.findall(pattern, content)
            return matches
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []
    
    def validate_html_templates(self):
        """Validate image paths in HTML templates"""
        print("Validating HTML templates...")
        
        # Patterns for different types of image references
        patterns = [
            r'static\([\'"](images/[^\'"]*)[\'"]\)',  # Django static tags
            r'src=[\'"](\.\./static/images/[^\'"]*)[\'"]',  # Relative static paths
            r'background-image:\s*url\([\'"]([^\'"]*)[\'"]\)',  # CSS backgrounds
            r'background-image:\s*url\(([^)]+)\)'  # CSS backgrounds without quotes
        ]
        
        for template_file in self.templates_dir.rglob('*.html'):
            for pattern in patterns:
                paths = self.extract_image_paths_from_file(template_file, pattern)
                for path in paths:
                    if not self.validate_static_path(path):
                        self.broken_links.append({
                            'file': str(template_file.relative_to(self.base_dir)),
                            'path': path,
                            'type': 'template'
                        })
                    else:
                        self.valid_links.append({
                            'file': str(template_file.relative_to(self.base_dir)),
                            'path': path,
                            'type': 'template'
                        })
    
    def validate_css_files(self):
        """Validate image paths in CSS files"""
        print("Validating CSS files...")
        
        css_dir = self.static_dir / 'css'
        patterns = [
            r'url\([\'"]([^\'"]*)[\'"]\)',
            r'url\(([^)]+)\)'
        ]
        
        for css_file in css_dir.rglob('*.css'):
            for pattern in patterns:
                paths = self.extract_image_paths_from_file(css_file, pattern)
                for path in paths:
                    # Skip data URLs and external URLs
                    if path.startswith(('data:', 'http:', 'https:', '//')):
                        continue
                    
                    if not self.validate_static_path(path):
                        self.broken_links.append({
                            'file': str(css_file.relative_to(self.base_dir)),
                            'path': path,
                            'type': 'css'
                        })
                    else:
                        self.valid_links.append({
                            'file': str(css_file.relative_to(self.base_dir)),
                            'path': path,
                            'type': 'css'
                        })
    
    def validate_python_files(self):
        """Validate image paths in Python files"""
        print("Validating Python files...")
        
        patterns = [
            r'static\([\'"](images/[^\'"]*)[\'"]\)',
            r'[\'"](images/[^\'"]*)[\'"]'
        ]
        
        for py_file in self.base_dir.rglob('*.py'):
            # Skip migrations and __pycache__
            if 'migrations' in str(py_file) or '__pycache__' in str(py_file):
                continue
                
            for pattern in patterns:
                paths = self.extract_image_paths_from_file(py_file, pattern)
                for path in paths:
                    if not self.validate_static_path(path):
                        self.broken_links.append({
                            'file': str(py_file.relative_to(self.base_dir)),
                            'path': path,
                            'type': 'python'
                        })
                    else:
                        self.valid_links.append({
                            'file': str(py_file.relative_to(self.base_dir)),
                            'path': path,
                            'type': 'python'
                        })
    
    def generate_report(self):
        """Generate a comprehensive validation report"""
        print(f"\n{'='*60}")
        print("IMAGE PATH VALIDATION REPORT")
        print(f"{'='*60}")
        
        print(f"\nValid Links: {len(self.valid_links)}")
        print(f"Broken Links: {len(self.broken_links)}")
        
        if self.broken_links:
            print(f"\n{'='*60}")
            print("BROKEN IMAGE LINKS FOUND:")
            print(f"{'='*60}")
            
            for i, link in enumerate(self.broken_links, 1):
                print(f"{i}. File: {link['file']}")
                print(f"   Path: {link['path']}")
                print(f"   Type: {link['type']}")
                print(f"   {'-'*40}")
        
        # Group broken links by type for summary
        by_type = {}
        for link in self.broken_links:
            by_type.setdefault(link['type'], []).append(link)
        
        print(f"\n{'='*60}")
        print("SUMMARY BY TYPE:")
        print(f"{'='*60}")
        for link_type, links in by_type.items():
            print(f"{link_type.upper()}: {len(links)} broken links")
    
    def run_validation(self):
        """Run complete validation"""
        print("Starting image path validation...")
        self.validate_html_templates()
        self.validate_css_files()
        self.validate_python_files()
        self.generate_report()
        
        return len(self.broken_links) == 0

def main():
    validator = SimpleImageValidator()
    success = validator.run_validation()
    
    if success:
        print("\n✅ All image paths are valid!")
        return 0
    else:
        print(f"\nFound {len(validator.broken_links)} broken image links!")
        return 1

if __name__ == "__main__":
    exit(main())