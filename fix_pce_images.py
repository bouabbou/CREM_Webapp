#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('c:/Users/HP/Desktop/CREM_Webapp')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CREM_Webapp.settings')
django.setup()

from django.templatetags.static import static

def fix_pce_innovation():
    """Fix PCE innovation image paths"""
    innovation_images = [
        'images/platforms/PCE/innovation_PCE/inno1.png',
        'images/platforms/PCE/innovation_PCE/inno2.png',
        'images/platforms/PCE/innovation_PCE/inno3.png',
        'images/platforms/PCE/innovation_PCE/inno4.png',
        'images/platforms/PCE/innovation_PCE/inno5.png',
        'images/platforms/PCE/innovation_PCE/inno6.jpg',
        'images/platforms/PCE/innovation_PCE/inno7.jpg',
        'images/platforms/PCE/innovation_PCE/inno8.png',
        'images/platforms/PCE/innovation_PCE/inno9.png'
    ]
    
    return [static(img) for img in innovation_images]

def fix_pce_services():
    """Fix PCE services image paths"""
    services_images = [
        'images/platforms/PCE/services_PCE/serv1.jpg',
        'images/platforms/PCE/services_PCE/serv2.jpg',
        'images/platforms/PCE/services_PCE/serv3.jpg',
        'images/platforms/PCE/services_PCE/serv4.jpg'
    ]
    
    return [static(img) for img in services_images]

if __name__ == "__main__":
    print("PCE Innovation Images:")
    for i, img in enumerate(fix_pce_innovation(), 1):
        print(f"Section {i}: {img}")
    
    print("\nPCE Services Images:")
    for i, img in enumerate(fix_pce_services(), 1):
        print(f"Section {i}: {img}")