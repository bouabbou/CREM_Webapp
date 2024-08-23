# CREM/views.py
from django.templatetags.static import static

from django.shortcuts import render
from django.urls import reverse


from instrumentation.models import Category, Product


#platfroms infrustructures

def ASMP_infrastructure(request):
    
    """
    View function to render the infrastructure page for the Advanced Manufacturing 
    Platform (ASMP). Fetches categories and products from the database, prepares context 
    data, and renders the 'infrastructure.html' template with the provided context.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML response for the 'infrastructure.html' template.
    """
    # Fetch categories and products from the database
    categories = Category.objects.all()
    products = Product.objects.all()

    # Context data to pass to the template
    context = {
        
        'categories': categories,
        'products': products,
        
        #Data to pass to the template
        'image_header': "Our advanced manufacturing platform",
        'image_descriptions': {
            'part1': "ADDITIVE MANUFACTURING",
            'part2': "CNC MACHINING",
            'part3': "COMPOSITES",
            'part4': "CHARACTERIZATION",
        },
        'header_img': "../static/images/revo-slider/infra.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Powder-Based",
                'subtitle': "Additive Manufacturing",
            },
            'section_2': {
                'title': "Fused deposition modeling",
                'subtitle': "Additive Manufacturing",
            },
            'section_3': {
                'title': "CNC Machinning",
                'subtitle': "Subtitle for Section 3",
            },
        },
        'platform_name': "ADDITIVE/SUBSTRACTIVE MANUFACTURING AND PROTOTYPING",
        'slider_image_url_1': "../static/images/flexslider/AMLAB1.jpg",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB2.png", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.jpg", 
        
        #header
        'services_url': reverse('ASMP_services'),
        'index_url': reverse('ASMP_index'),
        'Infrastructre_url': reverse('ASMP_infrastructure'),
        'innovation_url': reverse('ASMP_innovation'),
        'logo': '../../static/images/logo-grey.png',
        
        #platform filtration : 
        'platform_name' : "ADDITIVE/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM"
    }

    # Render the template with the context data
    return render(request, 'platforms/ASMP/ASMP_Infrastructure_FA_EN.html', context)
def BIO_infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'image_header': "Image Header",
        'image_descriptions': {
            'part1': "Description Part 1",
            'part2': "Description Part 2",
            'part3': "Description Part 3",
            'part4': "Description Part 4",
        },
        'header_img': "../static/images/revo-slider/infra.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Title for Section 1",
                'subtitle': "Subtitle for Section 1",
            },
            'section_2': {
                'title': "Title for Section 2",
                'subtitle': "Subtitle for Section 2",
            },
            'section_3': {
                'title': "Title for Section 3",
                'subtitle': "Subtitle for Section 3",
            },
        },
        'platform_name': "BIOTECHNOLOGY ET BIOMEDICAL ENGINEERING",
        'slider_image_url_1': "../static/images/flexslider/zAMLAB3.jpg",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.jpg", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.jpg", 
        'logo': '../../static/images/logo-grey.png',
        
        #header : 
        'services_url': reverse('BIO_services'),
        'index_url': reverse('BIO_index'),
        'infrastructure_url': reverse('BIO_infrastructure'),
        'innovation_url': reverse('BIO_innovation'),
        'logo': '../../static/images/logo-grey.png',
        


    }

    return render( request ,'platforms/BIO/BIO_infrastructure.html', context)
def MSC_infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'image_header': "Image Header",
        'image_descriptions': {
            'part1': "Description Part 1",
            'part2': "Description Part 2",
            'part3': "Description Part 3",
            'part4': "Description Part 4",
        },
        'header_img': "../static/images/revo-slider/infra.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Title for Section 1",
                'subtitle': "Subtitle for Section 1",
            },
            'section_2': {
                'title': "Title for Section 2",
                'subtitle': "Subtitle for Section 2",
            },
            'section_3': {
                'title': "Title for Section 3",
                'subtitle': "Subtitle for Section 3",
            },
        },
        'platform_name': "Materials, Synthesis, and Characterization Platform",
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.jpg",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.jpg", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.jpg",
        'logo': '../../static/images/logo-grey.png',
        
         #header : 
        'services_url': reverse('MSC_services'),
        'index_url': reverse('MSC_index'),
        'infrastructure_url': reverse('MSC_infrastructure'),
        'innovation_url': reverse('MSC_innovation'),
        'logo': '../../static/images/logo-grey.png',
 

    }

    return render( request ,'platforms/MSC/MSC_infrastructure.html', context)
def PCE_infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'image_header': "Image Header",
        'image_descriptions': {
            'part1': "Description Part 1",
            'part2': "Description Part 2",
            'part3': "Description Part 3",
            'part4': "Description Part 4",
        },
        'header_img': "../static/images/revo-slider/infra.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Title for Section 1",
                'subtitle': "Subtitle for Section 1",
            },
            'section_2': {
                'title': "Title for Section 2",
                'subtitle': "Subtitle for Section 2",
            },
            'section_3': {
                'title': "Title for Section 3",
                'subtitle': "Subtitle for Section 3",
            },
        },
        'platform_name': "PROCESS ENGINEERING AND CIVIL ENGINEERING",
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.jpg",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.jpg", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.jpg",
        'logo': '../../static/images/logo-grey.png',
        
         #header : 
        'services_url': reverse('PCE_services'),
        'index_url': reverse('PCE_index'),
        'infrastructure_url': reverse('PCE_infrastructure'),
        'innovation_url': reverse('PCE_innovation'),
        'logo': '../../static/images/logo-grey.png',
 

    }

    return render( request ,'platforms/PCE/PCE_infrastructure.html', context)
def RESEE_infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'image_header': "Image Header",
        'image_descriptions': {
            'part1': "Description Part 1",
            'part2': "RESEE Part 2",
            'part3': "Description Part 3",
            'part4': "Description Part 4",
        },
        'header_img': "../static/images/revo-slider/infra.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Title for Section 1",
                'subtitle': "Subtitle for Section 1",
            },
            'section_2': {
                'title': "Title for Section 2",
                'subtitle': "Subtitle for Section 2",
            },
            'section_3': {
                'title': "Title for Section 3",
                'subtitle': "Subtitle for Section 3",
            },
        },
        'platform_name': "ADDITIVE/SUBSTRACTIVE MANUFACTURING AND PROTOTYPING",
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.jpg", 
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.jpg", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.jpg", 
        'logo': '../../static/images/logo-grey.png',
        
         #header : 
        'services_url': reverse('RESEE_services'),
        'index_url': reverse('RESEE_index'),
        'infrastructure_url': reverse('RESEE_infrastructure'),
        'innovation_url': reverse('RESEE_innovation'),
        'logo': '../../static/images/logo-grey.png',



    }

    return render( request ,'platforms/RESEE/RESEE_infrastructure.html', context)
def SAI_infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'image_header': "Image Header",
        'image_descriptions': {
            'part1': "Description Part 1",
            'part2': "Description Part 2",
            'part3': "Description Part 3",
            'part4': "Description Part 4",
        },
        'header_img': "../static/images/revo-slider/infra.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Title for Section 1",
                'subtitle': "Subtitle for Section 1",
            },
            'section_2': {
                'title': "Title for Section 2",
                'subtitle': "Subtitle for Section 2",
            },
            'section_3': {
                'title': "Title for Section 3",
                'subtitle': "Subtitle for Section 3",
            },
        },
        'platform_name': "SENSORS AND INSTRUMENTATION",
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.jpg",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.jpg", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.jpg", 
        'logo': '../../static/images/logo-grey.png',
        
         #header : 
        'services_url': reverse('SAI_services'),
        'index_url': reverse('SAI_index'),
        'infrastructure_url': reverse('SAI_infrastructure'),
        'innovation_url': reverse('SAI_innovation'),
        'logo': '../../static/images/logo-grey.png',


    }

    return render( request ,'platforms/sai/SAI_infrastructure.html', context)
def AIDE_infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'image_header': "Image Header",
        'image_descriptions': {
            'part1': "Description Part 1",
            'part2': "Description Part 2",
            'part3': "Description Part 3",
            'part4': "Description Part 4",
        },
        'header_img': "../static/images/revo-slider/infra.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Title for Section 1",
                'subtitle': "Subtitle for Section 1",
            },
            'section_2': {
                'title': "Title for Section 2",
                'subtitle': "Subtitle for Section 2",
            },
            'section_3': {
                'title': "Title for Section 3",
                'subtitle': "Subtitle for Section 3",
            },
        },
        'platform_name': "AI AND DIGITAL ENGINEERING",
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.jpg",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.jpg", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.jpg", 
        'logo': '../../static/images/logo-grey.png',

        #header : 
        'services_url': reverse('AIDE_services'),
        'index_url': reverse('AIDE_index'),
        'infrastructure_url': reverse('AIDE_infrastructure'),
        'innovation_url': reverse('AIDE_innovation'),
        'logo': '../../static/images/logo-grey.png',

    }

    return render( request ,'platforms/AIDE/AIDE_infrastructure.html', context)


def home(request):
    return render( request ,'Home_EN.html')
def contact(request):
    return render( request ,'Contact_EN.html')
def ASMP_innovation(request):
    context = {
        'header1': {
            'title_1': 'ADDITIVE ',
            'title_2': ' MANUFACTURING',
        },
        'header2': {
            'title_1': 'SUBSTRACTIVE ',
            'title_2': ' MANUFACTURING',
        },
        'header3': {
            'title_1': 'COMPOSITE ',
            'title_2': ' MATERIALS',
        },
        'sections': {
            'section1': {
                'title': 'Laser Powder Bed Fusion',
                'tag': 'LPBF',
                'text': 'Our work in Laser Powder Bed Fusion (LPBF) centers on producing precise metal components. LPBF allows for intricate and customized geometries, enabling limitless innovation, especially in high-demand industries. ',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'Selective Laser Sintering',
                'tag': 'SLS',
                'text': 'Redefines polymer part manufacturing standards. This technology opens up new possibilities for complex geometries and designs in various industries.',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'FUSED DEPOSITION MODELING',
                'tag': 'FDM',
                'text': 'This technology efficiently produces thermoplastic parts. Suitable for both conceptual prototypes and functional components. Our work with FDM aims to optimize this popular 3D printing process.',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'STEREOLITHOGRAPHY',
                'tag': 'SLA',
                'text': 'Stereolithography (SLA) is resin-based 3D printing technologies with unparalleled precision. it s used for custom dental prosthetics, detailed designs or any high-precision part.',
                'img': '../static/images/Innovation/SLA.png'

            },
            'section5': {
                'title': 'CNC',
                'tag': 'MACHINING',
                'text': 'Our platform features CNC machining tools that produce metal, plastic, and other material parts with micrometer precision, meeting demanding quality and performance standards. ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'RAPID',
                'tag': 'TOOLING',
                'text': 'This approach is used for efficient manufacturing by quickly producing molds, dies, or other tooling components. It uses techniques like 3D printing and CNC machining for faster iterations and cost-effective production.',
                'img': '../static/images/Innovation/RP.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/Innovation/CF.png'
            }
        },
    
        # Additional context variables
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('ASMP_services'),
        'index_url': reverse('ASMP_index'),
        'infrastructure_url': reverse('ASMP_infrastructure'),
        'innovation_url': reverse('ASMP_innovation'),
        'img': '../static/images/logo-grey.png'
    }
    
    return render(request, 'platforms/ASMP/ASMP_Innovation_FA_EN.html', context)
def AIDE_innovation(request):
        
        #data 
    context = {
        'header1': {
            'title_1': 'header1 ',
            'title_2': ' title1',
        },
        'header2': {
            'title_1': 'header2 ',
            'title_2': ' title2',
        },
        'header3': {
            'title_1': 'header3 ',
            'title_2': ' title3',
        },
        'sections': {
            'section1': {
                'title': 'title 1',
                'tag': 'tag1',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'title 2',
                'tag': 'tag2',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'title 3',
                'tag': 'tag3',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'title 4',
                'tag': 'tag4',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/SLA.png'

            },
            'section5': {
                'title': 'title 5',
                'tag': 'tag5',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'title 6',
                'tag': 'tag6',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/Innovation/CF.png'
            }
        },
         #header
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('AIDE_services'),
        'index_url': reverse('AIDE_index'),
        'infrastructure_url': reverse('AIDE_infrastructure'),
        'innovation_url': reverse('AIDE_innovation'),
    }

    return render( request ,'platforms/AIDE/AIDE_innovation.html',context)


def RESEE_innovation(request):
    context = {
        'header1': {
            'title_1': 'header1 ',
            'title_2': ' title1',
        },
        'header2': {
            'title_1': 'header2 ',
            'title_2': ' title2',
        },
        'header3': {
            'title_1': 'header3 ',
            'title_2': ' title3',
        },
        'sections': {
            'section1': {
                'title': 'title 1',
                'tag': 'tag1',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'title 2',
                'tag': 'tag2',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'title 3',
                'tag': 'tag3',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'title 4',
                'tag': 'tag4',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/SLA.png'

            },
            'section5': {
                'title': 'title 5',
                'tag': 'tag5',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'title 6',
                'tag': 'tag6',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/Innovation/CF.png'
            }
        },
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('RESEE_services'),
        'index_url': reverse('RESEE_index'),
        'infrastructure_url': reverse('RESEE_infrastructure'),
        'innovation_url': reverse('RESEE_innovation'),
    }
    return render( request ,'platforms/RESEE/RESEE_innovation.html',context)


def BIO_innovation(request):
    context = {
        'header1': {
            'title_1': 'header1 ',
            'title_2': ' title1',
        },
        'header2': {
            'title_1': 'header2 ',
            'title_2': ' title2',
        },
        'header3': {
            'title_1': 'header3 ',
            'title_2': ' title3',
        },
        'sections': {
            'section1': {
                'title': 'title 1',
                'tag': 'tag1',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'title 2',
                'tag': 'tag2',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'title 3',
                'tag': 'tag3',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'title 4',
                'tag': 'tag4',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/SLA.png'

            },
            'section5': {
                'title': 'title 5',
                'tag': 'tag5',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'title 6',
                'tag': 'tag6',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/Innovation/CF.png'
            }
        },
        
        #header
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('BIO_services'),
        'index_url': reverse('BIO_index'),
        'infrastructure_url': reverse('BIO_infrastructure'),
        'innovation_url': reverse('BIO_innovation'),
    }
    return render( request ,'platforms/BIO/BIO_innovation.html',context)


def MSC_innovation(request):
    context = {
        #data
        'header1': {
            'title_1': 'header1 ',
            'title_2': ' title1',
        },
        'header2': {
            'title_1': 'header2 ',
            'title_2': ' title2',
        },
        'header3': {
            'title_1': 'header3 ',
            'title_2': ' title3',
        },
        'sections': {
            'section1': {
                'title': 'title 1',
                'tag': 'tag1',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'title 2',
                'tag': 'tag2',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'title 3',
                'tag': 'tag3',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'title 4',
                'tag': 'tag4',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/SLA.png'

            },
            'section5': {
                'title': 'title 5',
                'tag': 'tag5',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'title 6',
                'tag': 'tag6',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/Innovation/CF.png'
            }
        },
        
        #header
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('MSC_services'),
        'index_url': reverse('MSC_index'),
        'infrastructure_url': reverse('MSC_infrastructure'),
        'innovation_url': reverse('MSC_innovation'),
    }
    return render( request ,'platforms/MSC/MSC_innovation.html',context)


def PCE_innovation(request):
    context = {
        'header1': {
            'title_1': 'header1 ',
            'title_2': ' title1',
        },
        'header2': {
            'title_1': 'header2 ',
            'title_2': ' title2',
        },
        'header3': {
            'title_1': 'header3 ',
            'title_2': ' title3',
        },
        'sections': {
            'section1': {
                'title': 'title 1',
                'tag': 'tag1',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'title 2',
                'tag': 'tag2',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'title 3',
                'tag': 'tag3',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'title 4',
                'tag': 'tag4',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/SLA.png'

            },
            'section5': {
                'title': 'title 5',
                'tag': 'tag5',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'title 6',
                'tag': 'tag6',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/Innovation/CF.png'
            }
        },
        
        #header
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('PCE_services'),
        'index_url': reverse('PCE_index'),
        'infrastructure_url': reverse('PCE_infrastructure'),
        'innovation_url': reverse('PCE_innovation'),
    }
    return render( request ,'platforms/PCE/PCE_innovation.html',context)


def SAI_innovation(request):
    context = {
        'header1': {
            'title_1': 'header1 ',
            'title_2': ' title1',
        },
        'header2': {
            'title_1': 'header2 ',
            'title_2': ' title2',
        },
        'header3': {
            'title_1': 'header3 ',
            'title_2': ' title3',
        },
        'sections': {
            'section1': {
                'title': 'title 1',
                'tag': 'tag1',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'title 2',
                'tag': 'tag2',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'title 3',
                'tag': 'tag3',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'title 4',
                'tag': 'tag4',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/SLA.png'

            },
            'section5': {
                'title': 'title 5',
                'tag': 'tag5',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'title 6',
                'tag': 'tag6',
                'text': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/Innovation/CF.png'
            }
        },
        #header
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('SAI_services'),
        'index_url': reverse('SAI_index'),
        'infrastructure_url': reverse('SAI_infrastructure'),
        'innovation_url': reverse('SAI_innovation'),
    }
    return render( request ,'platforms/sai/SAI_innovation.html',context)

# platfrom's services

def ASMP_services(request):
    context = {
       'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('ASMP_services'),
        'index_url': reverse('ASMP_index'),
        'infrastructure_url': reverse('ASMP_infrastructure'),
        'innovation_url': reverse('ASMP_innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': '3D',
            'title_line2': 'DESIGN',
            'text': 'Our 3D Design and reverse engineering services empower you to create exceptional 3D models, transforming your ideas into reality.',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../../static/images/Serv/7.jpeg'

        },
    },
    }
    return render( request ,'platforms/ASMP/ASMP_Services_FA_EN.html',context)
def AIDE_services(request):
    context = {
       'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('AIDE_services'),
        'index_url': reverse('AIDE_index'),
        'infrastructure_url': reverse('AIDE_infrastructure'),
        'innovation_url': reverse('AIDE_innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': '3D',
            'title_line2': 'DESIGN',
            'text': 'Our 3D Design and reverse engineering services empower you to create exceptional 3D models, transforming your ideas into reality.',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../../static/images/Serv/7.jpeg'

        },
    },
    }
    return render( request ,'platforms/AIDE/AIDE_services.html',context)
def BIO_services(request):
    context = {
       'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('BIO_services'),
        'index_url': reverse('BIO_index'),
        'infrastructure_url': reverse('BIO_infrastructure'),
        'innovation_url': reverse('BIO_innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': '3D',
            'title_line2': 'DESIGN',
            'text': 'Our 3D Design and reverse engineering services empower you to create exceptional 3D models, transforming your ideas into reality.',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../../static/images/Serv/7.jpeg'

        },
    },
    }
    return render( request ,'platforms/BIO/BIO_services.html',context)
def MSC_services(request):
    context = {
       'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('MSC_services'),
        'index_url': reverse('MSC_index'),
        'infrastructure_url': reverse('MSC_infrastructure'),
        'innovation_url': reverse('MSC_innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': '3D',
            'title_line2': 'DESIGN',
            'text': 'Our 3D Design and reverse engineering services empower you to create exceptional 3D models, transforming your ideas into reality.',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../../static/images/Serv/7.jpeg'

        },
    },
    }
    return render( request ,'platforms/MSC/MSC_services.html',context)
def PCE_services(request):
    context = {
       'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('PCE_services'),
        'index_url': reverse('PCE_index'),
        'infrastructure_url': reverse('PCE_infrastructure'),
        'innovation_url': reverse('PCE_innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': '3D',
            'title_line2': 'DESIGN',
            'text': 'Our 3D Design and reverse engineering services empower you to create exceptional 3D models, transforming your ideas into reality.',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../../static/images/Serv/7.jpeg'

        },
    },
    }

    return render( request ,'platforms/PCE/PCE_services.html',context)
def RESEE_services(request):
    context = {
       'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('RESEE_services'),
        'index_url': reverse('RESEE_index'),
        'infrastructure_url': reverse('RESEE_infrastructure'),
        'innovation_url': reverse('RESEE_innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': '3D',
            'title_line2': 'DESIGN',
            'text': 'Our 3D Design and reverse engineering services empower you to create exceptional 3D models, transforming your ideas into reality.',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../../static/images/Serv/7.jpeg'

        },
    },
    }
    return render( request ,'platforms/RESEE/RESEE_services.html',context)
def SAI_services(request):
    context = {
       'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('SAI_services'),
        'index_url': reverse('SAI_index'),
        'infrastructure_url': reverse('SAI_infrastructure'),
        'innovation_url': reverse('SAI_innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': '3D',
            'title_line2': 'DESIGN',
            'text': 'Our 3D Design and reverse engineering services empower you to create exceptional 3D models, transforming your ideas into reality.',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../../static/images/Serv/7.jpeg'

        },
    },
    }
    
    return render( request ,'platforms/sai/SAI_services.html',context)


# platforms presentation
def ASMP_index(request):
    context = {
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/ASMP.mp4",
        "title": "ADDITIVE/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM",
        "description": "Advanced technologies, materials expertise, and practical knowledge in one place."
    },
    "about": {
        "text_1": "Our additive and subtractive manufacturing platform offers versatility, enabling rapid production of prototypes and functional parts across industries such as aerospace, automotive, and biomedical. We are committed to advancing materials science and shaping the future of manufacturing.",
        "text_2": "Our platform integrates both subtractive and additive manufacturing techniques to produce complex functional parts across various industrial sectors. We work with a range of materials, including Polymers, Metals, Composites, Ceramics, and Concrete."
    },
    "third_section": {
        "title": "Additive Manufacturing Advantages",
        "description": "Additive manufacturing offers numerous benefits, including the ability to create complex geometries, customize products, and use a variety of materials.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Geometric Complexity",
            "description": "It allows the realization of complex geometries that were previously unattainable using traditional manufacturing methods."
        },
        "point_2": {
            "title": "Personalization",
            "description": "It enables the production of customized and unique objects tailored to the specific needs of each user or application."
        },
        "point_3": {
            "title": "Material Diversity",
            "description": "Using a diverse range of materials, including plastics, metals, and composites, AM provides flexibility in material selection for creating innovative objects."
        },
        "point_4": {
            "title": "Rapid Prototyping",
            "description": "3D printing allows for rapid prototyping, which accelerates the product development process, thus minimizing the associated costs."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/ASMP_PLATFORM.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At CREM, we harness cutting-edge technologies to advance progress and innovation across diverse industrial sectors:",
        "tab_1": {
            "header": "Aerospace",
            "title": "A New Era of Creation in Aerospace",
            "description": "Within the aerospace industry, a transformative era of producing intricate components, previously challenging with conventional methods, is now attainable through additive manufacturing.From lightweight components to rocket engines, the potential for innovation is limitless.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Automotive",
            "title": "Transforming Automotive Manufacturing",
            "description": "From polymer-based composites tailored for specific automotive structures to customized metal parts made through 3D printing, modern manufacturing advancements enable part customization, cost and lead time reduction, as well as the creation of lighter structures and innovative geometries.",
           
        },
        "tab_3": {
            "header": "Medical Technology",
            "title": "Precision Healthcare: Custom Solutions with Additive Manufacturing",
            "description": "Additive manufacturing is revolutionizing healthcare, through personalized medical solutions, from tailored implants to custom prosthetics.By leveraging this innovative technology, healthcare providers can now fabricate customized implants, prosthetics and other medical devices that are meticulously designed to meet the unique requirements of each patient, driving enhanced outcomes.",
           
        },
        "tab_4": {
            "header": "Other Industries",
            "title": "The Diverse Applications of Additive Manufacturing Across Industries",
            "description": "From mechanical engineering to construction, tool-making, art, fashion, and lifestyle, 3D printing is revolutionizing a multitude of industries.\nThe versatility of additive manufacturing is driving innovation by empowering businesses and artists to explore new creative possibilities, unlock novel creative avenues, enhance efficiency, and redefine the standards within their industries."
          
        }
    },
    
     #header : 
        'services_url': reverse('ASMP_services'),
        'index_url': reverse('ASMP_index'),
        'infrastructure_url': reverse('ASMP_infrastructure'),
        'innovation_url': reverse('ASMP_innovation'),
        'logo': '../static/images/logo-white.png',
}

    
    return render( request ,'platforms/ASMP/ASMP_index_FA_EN.html',context)

def BIO_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/BIO.mp4",
        "title": "BIO/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM",
        "description": "Advanced technologies, materials expertise, and practical knowledge in one place."
    },
    "about": {
        "text_1": "Our additive and subtractive manufacturing platform offers versatility, enabling rapid production of prototypes and functional parts across industries such as aerospace, automotive, and biomedical. We are committed to advancing materials science and shaping the future of manufacturing.",
        "text_2": "Our platform integrates both subtractive and additive manufacturing techniques to produce complex functional parts across various industrial sectors. We work with a range of materials, including Polymers, Metals, Composites, Ceramics, and Concrete."
    },
    "third_section": {
        "title": "Additive Manufacturing Advantages",
        "description": "Additive manufacturing offers numerous benefits, including the ability to create complex geometries, customize products, and use a variety of materials.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Geometric Complexity",
            "description": "It allows the realization of complex geometries that were previously unattainable using traditional manufacturing methods."
        },
        "point_2": {
            "title": "Personalization",
            "description": "It enables the production of customized and unique objects tailored to the specific needs of each user or application."
        },
        "point_3": {
            "title": "Material Diversity",
            "description": "Using a diverse range of materials, including plastics, metals, and composites, AM provides flexibility in material selection for creating innovative objects."
        },
        "point_4": {
            "title": "Rapid Prototyping",
            "description": "3D printing allows for rapid prototyping, which accelerates the product development process, thus minimizing the associated costs."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/BIO.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At CREM, we harness cutting-edge technologies to advance progress and innovation across diverse industrial sectors:",
        "tab_1": {
            "header": "Aerospace",
            "title": "A New Era of Creation in Aerospace",
            "description": "Within the aerospace industry, a transformative era of producing intricate components, previously challenging with conventional methods, is now attainable through additive manufacturing.From lightweight components to rocket engines, the potential for innovation is limitless.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Automotive",
            "title": "Transforming Automotive Manufacturing",
            "description": "From polymer-based composites tailored for specific automotive structures to customized metal parts made through 3D printing, modern manufacturing advancements enable part customization, cost and lead time reduction, as well as the creation of lighter structures and innovative geometries.",
           
        },
        "tab_3": {
            "header": "Medical Technology",
            "title": "Precision Healthcare: Custom Solutions with Additive Manufacturing",
            "description": "Additive manufacturing is revolutionizing healthcare, through personalized medical solutions, from tailored implants to custom prosthetics.By leveraging this innovative technology, healthcare providers can now fabricate customized implants, prosthetics and other medical devices that are meticulously designed to meet the unique requirements of each patient, driving enhanced outcomes.",
           
        },
        "tab_4": {
            "header": "Other Industries",
            "title": "The Diverse Applications of Additive Manufacturing Across Industries",
            "description": "From mechanical engineering to construction, tool-making, art, fashion, and lifestyle, 3D printing is revolutionizing a multitude of industries.\nThe versatility of additive manufacturing is driving innovation by empowering businesses and artists to explore new creative possibilities, unlock novel creative avenues, enhance efficiency, and redefine the standards within their industries."
          
        }
    },
     #header : 
        'services_url': reverse('BIO_services'),
        'index_url': reverse('BIO_index'),
        'infrastructure_url': reverse('BIO_infrastructure'),
        'innovation_url': reverse('BIO_innovation'),

}
    return render( request ,'platforms/BIO/BIO_index.html', context)

def MSC_index(request):
    context = {
        
        "header": {
        "video": "../static/video/MSC.mp4",
        "title": "Materials, Synthesis, and Characterization Platform",
        "description": "",
    },
    "about": {
        "text_1": "Our additive and subtractive manufacturing platform offers versatility, enabling rapid production of prototypes and functional parts across industries such as aerospace, automotive, and biomedical. We are committed to advancing materials science and shaping the future of manufacturing.",
        "text_2": "Our platform analyzes various parameters such as crystallinity, specific surface area, morphology, chemical composition, particle size distribution, density, and moisture content. In mechanical characterization, we assess material response to stress, including elasticity, hardness, toughness, and fatigue resistance."
    },
    "third_section": {
        "title": "Innovative Material Characterization",
        "description": "desctiption",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Precision Measurement",
            "description": "Our platform integrates cutting-edge technology, offering precise and reliable measurements across a wide range of material applications."
        },
        "point_2": {
            "title": "Advanced Analytical Techniques",
            "description": "Employing state-of-the-art methods like Nuclear Magnetic Resonance (NMR) and X-Ray Diffraction (XRD), we push the boundaries of material science."
        },
        "point_3": {
            "title": "Comprehensive Support",
            "description": "Beyond instrumentation, we provide unparalleled support and expertise, ensuring you navigate the complexities of material characterization with ease."
        },
        "point_4": {
            "title": "Customized Solutions",
            "description": "Tailored to meet specific research and industrial needs, our solutions enhance efficiency and drive innovation in material science."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/MSC.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At CREM, we harness cutting-edge technologies to advance progress and innovation across diverse industrial sectors:",
        "tab_1": {
            "header": "Aerospace",
            "title": "A New Era of Creation in Aerospace",
            "description": "Within the aerospace industry, a transformative era of producing intricate components, previously challenging with conventional methods, is now attainable through additive manufacturing.From lightweight components to rocket engines, the potential for innovation is limitless.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Automotive",
            "title": "Transforming Automotive Manufacturing",
            "description": "From polymer-based composites tailored for specific automotive structures to customized metal parts made through 3D printing, modern manufacturing advancements enable part customization, cost and lead time reduction, as well as the creation of lighter structures and innovative geometries.",
           
        },
        "tab_3": {
            "header": "Medical Technology",
            "title": "Precision Healthcare: Custom Solutions with Additive Manufacturing",
            "description": "Additive manufacturing is revolutionizing healthcare, through personalized medical solutions, from tailored implants to custom prosthetics.By leveraging this innovative technology, healthcare providers can now fabricate customized implants, prosthetics and other medical devices that are meticulously designed to meet the unique requirements of each patient, driving enhanced outcomes.",
           
        },
        "tab_4": {
            "header": "Other Industries",
            "title": "The Diverse Applications of Additive Manufacturing Across Industries",
            "description": "From mechanical engineering to construction, tool-making, art, fashion, and lifestyle, 3D printing is revolutionizing a multitude of industries.\nThe versatility of additive manufacturing is driving innovation by empowering businesses and artists to explore new creative possibilities, unlock novel creative avenues, enhance efficiency, and redefine the standards within their industries."
          
        }
    },
     #header : 
        'services_url': reverse('MSC_services'),
        'index_url': reverse('MSC_index'),
        'infrastructure_url': reverse('MSC_infrastructure'),
        'innovation_url': reverse('MSC_innovation'),
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
}

    
    return render( request ,'platforms/MSC/MSC_index.html',context)

def PCE_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/PCE.mp4",
        "title": "noyl",
        "description": "Advanced technologies, materials expertise, and practical knowledge in one place."
    },
    "about": {
        "text_1": "Our additive and subtractive manufacturing platform offers versatility, enabling rapid production of prototypes and functional parts across industries such as aerospace, automotive, and biomedical. We are committed to advancing materials science and shaping the future of manufacturing.",
        "text_2": "Our platform integrates both subtractive and additive manufacturing techniques to produce complex functional parts across various industrial sectors. We work with a range of materials, including Polymers, Metals, Composites, Ceramics, and Concrete."
    },
    "third_section": {
        "title": "Additive Manufacturing Advantages",
        "description": "Additive manufacturing offers numerous benefits, including the ability to create complex geometries, customize products, and use a variety of materials.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Geometric Complexity",
            "description": "It allows the realization of complex geometries that were previously unattainable using traditional manufacturing methods."
        },
        "point_2": {
            "title": "Personalization",
            "description": "It enables the production of customized and unique objects tailored to the specific needs of each user or application."
        },
        "point_3": {
            "title": "Material Diversity",
            "description": "Using a diverse range of materials, including plastics, metals, and composites, AM provides flexibility in material selection for creating innovative objects."
        },
        "point_4": {
            "title": "Rapid Prototyping",
            "description": "3D printing allows for rapid prototyping, which accelerates the product development process, thus minimizing the associated costs."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/PCE.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At CREM, we harness cutting-edge technologies to advance progress and innovation across diverse industrial sectors:",
        "tab_1": {
            "header": "Aerospace",
            "title": "A New Era of Creation in Aerospace",
            "description": "Within the aerospace industry, a transformative era of producing intricate components, previously challenging with conventional methods, is now attainable through additive manufacturing.From lightweight components to rocket engines, the potential for innovation is limitless.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Automotive",
            "title": "Transforming Automotive Manufacturing",
            "description": "From polymer-based composites tailored for specific automotive structures to customized metal parts made through 3D printing, modern manufacturing advancements enable part customization, cost and lead time reduction, as well as the creation of lighter structures and innovative geometries.",
           
        },
        "tab_3": {
            "header": "Medical Technology",
            "title": "Precision Healthcare: Custom Solutions with Additive Manufacturing",
            "description": "Additive manufacturing is revolutionizing healthcare, through personalized medical solutions, from tailored implants to custom prosthetics.By leveraging this innovative technology, healthcare providers can now fabricate customized implants, prosthetics and other medical devices that are meticulously designed to meet the unique requirements of each patient, driving enhanced outcomes.",
           
        },
        "tab_4": {
            "header": "Other Industries",
            "title": "The Diverse Applications of Additive Manufacturing Across Industries",
            "description": "From mechanical engineering to construction, tool-making, art, fashion, and lifestyle, 3D printing is revolutionizing a multitude of industries.\nThe versatility of additive manufacturing is driving innovation by empowering businesses and artists to explore new creative possibilities, unlock novel creative avenues, enhance efficiency, and redefine the standards within their industries."
          
        }
    },
     #header : 
      #  'services_url': reverse('PCE_services'),
        'index_url': reverse('PCE_index'),
        'infrastructure_url': reverse('PCE_infrastructure'),
        'innovation_url': reverse('PCE_innovation'),
        'logo': '../../static/images/logo-white.png',
}
    return render( request ,'platforms/PCE//PCE_index.html', context)

def RESEE_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/RESEE.mp4",
        "title": "ADDITIVE/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM",
        "description": "Advanced technologies, materials expertise, and practical knowledge in one place."
    },
    "about": {
        "text_1": "Our additive and subtractive manufacturing platform offers versatility, enabling rapid production of prototypes and functional parts across industries such as aerospace, automotive, and biomedical. We are committed to advancing materials science and shaping the future of manufacturing.",
        "text_2": "Our platform integrates both subtractive and additive manufacturing techniques to produce complex functional parts across various industrial sectors. We work with a range of materials, including Polymers, Metals, Composites, Ceramics, and Concrete."
    },
    "third_section": {
        "title": "Additive Manufacturing Advantages",
        "description": "Additive manufacturing offers numerous benefits, including the ability to create complex geometries, customize products, and use a variety of materials.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Geometric Complexity",
            "description": "It allows the realization of complex geometries that were previously unattainable using traditional manufacturing methods."
        },
        "point_2": {
            "title": "Personalization",
            "description": "It enables the production of customized and unique objects tailored to the specific needs of each user or application."
        },
        "point_3": {
            "title": "Material Diversity",
            "description": "Using a diverse range of materials, including plastics, metals, and composites, AM provides flexibility in material selection for creating innovative objects."
        },
        "point_4": {
            "title": "Rapid Prototyping",
            "description": "3D printing allows for rapid prototyping, which accelerates the product development process, thus minimizing the associated costs."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/RESEE.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At CREM, we harness cutting-edge technologies to advance progress and innovation across diverse industrial sectors:",
        "tab_1": {
            "header": "Aerospace",
            "title": "A New Era of Creation in Aerospace",
            "description": "Within the aerospace industry, a transformative era of producing intricate components, previously challenging with conventional methods, is now attainable through additive manufacturing.From lightweight components to rocket engines, the potential for innovation is limitless.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Automotive",
            "title": "Transforming Automotive Manufacturing",
            "description": "From polymer-based composites tailored for specific automotive structures to customized metal parts made through 3D printing, modern manufacturing advancements enable part customization, cost and lead time reduction, as well as the creation of lighter structures and innovative geometries.",
           
        },
        "tab_3": {
            "header": "Medical Technology",
            "title": "Precision Healthcare: Custom Solutions with Additive Manufacturing",
            "description": "Additive manufacturing is revolutionizing healthcare, through personalized medical solutions, from tailored implants to custom prosthetics.By leveraging this innovative technology, healthcare providers can now fabricate customized implants, prosthetics and other medical devices that are meticulously designed to meet the unique requirements of each patient, driving enhanced outcomes.",
           
        },
        "tab_4": {
            "header": "Other Industries",
            "title": "The Diverse Applications of Additive Manufacturing Across Industries",
            "description": "From mechanical engineering to construction, tool-making, art, fashion, and lifestyle, 3D printing is revolutionizing a multitude of industries.\nThe versatility of additive manufacturing is driving innovation by empowering businesses and artists to explore new creative possibilities, unlock novel creative avenues, enhance efficiency, and redefine the standards within their industries."
          
        }
    },
     #header : 
        'services_url': reverse('RESEE_services'),
        'index_url': reverse('RESEE_index'),
        'infrastructure_url': reverse('RESEE_infrastructure'),
        'innovation_url': reverse('RESEE_innovation'),
}

    
    return render( request ,'platforms/RESEE/RESEE_index.html',context)

def SAI_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/SAI.mp4",
        "title": "ADDITIVE/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM",
        "description": "Advanced technologies, materials expertise, and practical knowledge in one place."
    },
    "about": {
        "text_1": "Our additive and subtractive manufacturing platform offers versatility, enabling rapid production of prototypes and functional parts across industries such as aerospace, automotive, and biomedical. We are committed to advancing materials science and shaping the future of manufacturing.",
        "text_2": "Our platform integrates both subtractive and additive manufacturing techniques to produce complex functional parts across various industrial sectors. We work with a range of materials, including Polymers, Metals, Composites, Ceramics, and Concrete."
    },
    "third_section": {
        "title": "Additive Manufacturing Advantages",
        "description": "Additive manufacturing offers numerous benefits, including the ability to create complex geometries, customize products, and use a variety of materials.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Geometric Complexity",
            "description": "It allows the realization of complex geometries that were previously unattainable using traditional manufacturing methods."
        },
        "point_2": {
            "title": "Personalization",
            "description": "It enables the production of customized and unique objects tailored to the specific needs of each user or application."
        },
        "point_3": {
            "title": "Material Diversity",
            "description": "Using a diverse range of materials, including plastics, metals, and composites, AM provides flexibility in material selection for creating innovative objects."
        },
        "point_4": {
            "title": "Rapid Prototyping",
            "description": "3D printing allows for rapid prototyping, which accelerates the product development process, thus minimizing the associated costs."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/SAI.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At CREM, we harness cutting-edge technologies to advance progress and innovation across diverse industrial sectors:",
        "tab_1": {
            "header": "Aerospace",
            "title": "A New Era of Creation in Aerospace",
            "description": "Within the aerospace industry, a transformative era of producing intricate components, previously challenging with conventional methods, is now attainable through additive manufacturing.From lightweight components to rocket engines, the potential for innovation is limitless.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Automotive",
            "title": "Transforming Automotive Manufacturing",
            "description": "From polymer-based composites tailored for specific automotive structures to customized metal parts made through 3D printing, modern manufacturing advancements enable part customization, cost and lead time reduction, as well as the creation of lighter structures and innovative geometries.",
           
        },
        "tab_3": {
            "header": "Medical Technology",
            "title": "Precision Healthcare: Custom Solutions with Additive Manufacturing",
            "description": "Additive manufacturing is revolutionizing healthcare, through personalized medical solutions, from tailored implants to custom prosthetics.By leveraging this innovative technology, healthcare providers can now fabricate customized implants, prosthetics and other medical devices that are meticulously designed to meet the unique requirements of each patient, driving enhanced outcomes.",
           
        },
        "tab_4": {
            "header": "Other Industries",
            "title": "The Diverse Applications of Additive Manufacturing Across Industries",
            "description": "From mechanical engineering to construction, tool-making, art, fashion, and lifestyle, 3D printing is revolutionizing a multitude of industries.\nThe versatility of additive manufacturing is driving innovation by empowering businesses and artists to explore new creative possibilities, unlock novel creative avenues, enhance efficiency, and redefine the standards within their industries."
          
        }
    },
     #header : 
        'services_url': reverse('SAI_services'),
        'index_url': reverse('SAI_index'),
        'infrastructure_url': reverse('SAI_infrastructure'),
        'innovation_url': reverse('SAI_innovation'),
        'logo': '../../static/images/logo-white.png',
}

    
    return render( request , 'platforms/sai/SAI_index.html',context)

def AIDE_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        "header": {
        "video": "../static/video/AIDE.mp4",
        "title": "Virtual Reality and Collaborative Robotics AI Platform",
        "description": "Empowering innovation through immersive technologies and intelligent collaboration."
        },
       "about": {
        "text_1": "Our digital platform integrates three essential components, each meticulously designed to meet the highest standards of modern industry. First, our AI infrastructure is purpose-built to deliver exceptional computational power, crucial for running deep learning algorithms efficiently. Second, our virtual and augmented reality lab enables the development of immersive programs tailored to various sectors, from education to industrial training. Lastly, our robotics lab allows for the programming and simulation of diverse types of robots, including humanoids, paving the way for innovative human-machine collaboration.",
        "text_2": "Our platform seamlessly integrates advanced artificial intelligence, virtual reality, and collaborative robotics to revolutionize various industrial sectors. We specialize in leveraging cutting-edge AI algorithms, creating immersive VR and AR experiences, and developing sophisticated robotics solutions, including humanoids. Our multidisciplinary approach ensures that we deliver innovative, practical, and impactful solutions tailored to meet the specific needs of each industry."
    },
    "third_section": {
        "title": "Artificial intelligence and robotics",
        "description": "Artificial intelligence and robotics are transformative technologies that enhance automation, decision-making, and human-robot interaction across various industries. These technologies provide unprecedented capabilities in processing data, creating immersive experiences, and developing sophisticated robotic systems.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Enhanced Decision-Making",
            "description": "AI enables the analysis of vast amounts of data to make informed decisions, optimizing processes and improving efficiency."
        },
        "point_2": {
            "title": "Immersive Experiences",
            "description": "Virtual and augmented reality technologies create immersive environments that enhance training, education, and user engagement."
        },
        "point_3": {
            "title": "Human-Robot Collaboration",
            "description": "Collaborative robotics, or cobots, work alongside humans, increasing productivity and safety in the workplace by handling repetitive or hazardous tasks."
        },
        "point_4": {
            "title": "Advanced Simulation and Prototyping",
            "description": "Robotics and AI facilitate advanced simulation and prototyping, accelerating the development process and reducing costs by allowing virtual testing and iteration before physical implementation."
        }
    },
    "video": {
        "title_l": "Artificial",
        "title_r": "Intelligence",
        "video": "../static/video/AIDE.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At our platform, we leverage cutting-edge technologies to drive progress and innovation across various industrial sectors:",
        "tab_1": {
            "header": "Automative / Aerospace",
            "title": "REVOLUTIONIZING MANUFACTURING",
            "description": "Our AI and robotics solutions enhance precision and efficiency in the automotive/aerospace sector, enabling the production of complex parts and improving assembly line automation.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Medical Technology",
            "title": "ADVANCING HEALTHCARE",
            "description": "Our platform supports the creation of customized medical devices and prosthetics, as well as the development of immersive training programs for healthcare professionals.",
           
        },
        "tab_3": {
            "header": "Manufacturing",
            "title": "OPTIMIZING PRODUCTION",
            "description": "In manufacturing, our technologies streamline processes, improve quality control, and enable the development of innovative products through advanced prototyping and automation.",
           
        },
        "tab_4": {
            "header": "Logistics",
            "title": "ENHANCING EFFICIENCY",
            "description": "Our AI-driven solutions optimize logistics and supply chain management, ensuring timely deliveries and reducing operational costs."
          
        },
        "tab_5": {
            "header": "Education and Training",
            "title": "IMMERSIVE LEARNING",
            "description": "Our virtual and augmented reality technologies create immersive educational experiences, enhancing learning outcomes and providing realistic training simulations."
          
        },
        "tab_6": {
            "header": "Entertainment",
            "title": "TRANSFORMING EXPERIENCES",
            "description": "Our AI and VR/AR technologies revolutionize the entertainment industry, creating interactive and immersive experiences for audiences worldwide."
          
        }
    },
     #header :
        'services_url': reverse('AIDE_services'),
        'index_url': reverse('AIDE_index'),
        'infrastructure_url': reverse('AIDE_infrastructure'),
        'innovation_url': reverse('AIDE_innovation'),
        'logo': '../../static/images/logo-white.png',
}

    
    return render( request , 'platforms/AIDE/AIDE_index.html',context)

def presentation(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
    }
    return render( request , 'index_FA_EN.html',context)