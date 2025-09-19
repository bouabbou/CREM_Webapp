# Image Management Guide for CREM Webapp

## Overview
This guide provides best practices for managing images in the CREM Webapp to ensure optimal performance, proper presentation, and maintainability.

## Directory Structure

### Platform Images
```
static/images/platforms/
├── AIDE/
│   ├── index_AIDE/          # Platform homepage images
│   ├── infrastructure_AIDE/ # Infrastructure section images
│   ├── innovation_AIDE/     # Innovation section images
│   └── services_AIDE/       # Services section images
├── ASMP/
├── BIO/
├── MSC/
├── PCE/
├── RESEE/
└── sai/
```

### General Images
```
static/images/
├── Serv/                    # Service-related images
├── static-media/            # Static media assets
├── favicon/                 # Favicon and app icons
├── flexslider/              # Slider images
├── owl-carousel/            # Carousel images
└── revo-slider/             # Revolution slider images
```

## Best Practices

### 1. Image Formats
- **JPEG**: Use for photographs and complex images with many colors
- **PNG**: Use for images with transparency or simple graphics
- **WebP**: Preferred modern format (provide fallbacks for older browsers)
- **SVG**: Use for logos, icons, and simple graphics

### 2. Image Optimization
- Compress all images before uploading
- Use appropriate dimensions (don't scale large images with CSS)
- Implement responsive images with srcset for different screen sizes

### 3. Naming Conventions
- Use descriptive, lowercase names with hyphens: `platform-bg.jpg`
- Include platform prefix: `AIDE-services-bg.jpg`
- Use consistent numbering: `srv1.jpg`, `srv2.jpg`, etc.

### 4. CSS Background Images
- Use relative paths from CSS directory: `../images/platforms/AIDE/index_AIDE/bg.jpg`
- Implement fallback mechanisms for missing images
- Use platform-specific CSS classes: `.work-proc-1-bg-AIDE`

### 5. Template Images
- Use Django static template tags: `{% static 'images/path/to/image.jpg' %}`
- Provide alt text for accessibility
- Use lazy loading for better performance

## Common Issues and Solutions

### Broken Image Links
1. **Check file existence**: Verify images exist in the correct directory
2. **Path validation**: Use the validation script: `python scripts/simple_image_validator.py`
3. **Relative paths**: Ensure CSS paths are relative to the CSS file location

### Missing Directories
If these directories don't exist, create them:
- `static/images/Innovation/`
- `static/images/recherche/`

### Platform-Specific Backgrounds
Each platform should have these background images:
- `index_[PLATFORM]/[PLATFORM]-bg.jpg` - Main platform background
- `index_[PLATFORM]/work-proc-bg.jpg` - Work process background
- `index_[PLATFORM]/section3.jpg` - Third section image

## Validation Script
The project includes a validation script to check for broken image links:

```bash
python scripts/simple_image_validator.py
```

The script will:
- Validate HTML templates, CSS files, and Python files
- Report broken image links with file locations
- Provide summary statistics

## Performance Optimization

### Lazy Loading
Implement lazy loading for images below the fold:
```html
<img src="image.jpg" loading="lazy" alt="Description">
```

### Responsive Images
Use srcset for different screen sizes:
```html
<img srcset="image-320w.jpg 320w,
             image-480w.jpg 480w,
             image-800w.jpg 800w"
     sizes="(max-width: 320px) 280px,
            (max-width: 480px) 440px,
            800px"
     src="image-800w.jpg" alt="Description">
```

### Modern Formats
Provide WebP with JPEG fallback:
```html
<picture>
  <source type="image/webp" srcset="image.webp">
  <source type="image/jpeg" srcset="image.jpg">
  <img src="image.jpg" alt="Description">
</picture>
```

## Maintenance Checklist
- [ ] Regularly run validation script
- [ ] Optimize new images before uploading
- [ ] Update documentation when adding new image types
- [ ] Test all platform pages after image changes
- [ ] Monitor page load performance

## Troubleshooting

### Images Not Loading
1. Check browser console for 404 errors
2. Verify file permissions
3. Check Django static files configuration
4. Run `python manage.py collectstatic` if needed

### CSS Background Issues
1. Verify image paths are relative to CSS file
2. Check that images exist
3. Test background properties in browser dev tools

### Template Variable Issues
Template variables like `{{ third_section.image }}` require proper context data in Django views.