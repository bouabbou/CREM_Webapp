# CREM/views.py
from django.templatetags.static import static

from django.shortcuts import render
from django.urls import reverse


from instrumentation.models import Category, Product


#platfroms infrustructures

def ASMP_infrastructure(request):
    # Fetch categories and products from the database
    categories = Category.objects.all()
    products = Product.objects.all()

    # Context data to pass to the template
    context = {
        'categories': categories,
        'products': products,
        'services_url': reverse('ASMP_services'),
        'index_url': reverse('ASMP_index'),
        'Infrastructre_url': reverse('ASMP_infrastructure'),
        'innovation_url': reverse('ASMP_innovation'),
        'logo': '../../static/images/logo-grey.png',
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
        'platform_name': "ADDITIVE/SUBSTRACTIVE MANUFACTURING AND PROTOTYPING",
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.jpg",  
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
        'platform_name': "ADDITIVE/SUBSTRACTIVE MANUFACTURING AND PROTOTYPING",
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
        'platform_name': "ADDITIVE/SUBSTRACTIVE MANUFACTURING AND PROTOTYPING",
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
        'platform_name': "ADDITIVE/SUBSTRACTIVE MANUFACTURING AND PROTOTYPING",
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
        'platform_name': "Virtual Reality and Collaborative Robotics AI Platform",
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
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('ASMP_services'),
        'index_url': reverse('ASMP_index'),
        'infrastructure_url': reverse('ASMP_infrastructure'),
        'innovation_url': reverse('ASMP_innovation'),
    }
    return render( request ,'platforms/ASMP/ASMP_Innovation_FA_EN.html',context)
def AIDE_innovation(request):
    context = {
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
            'fest1_img': 'fes1-img'
            
        },
        'section_2': {
            'title_line1': 'ADDITIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Explore the infinite possibilities of additive manufacturing using cutting-edge technologies such as LPBF for metals, SLS for ceramics and polymers, FDM for thermoplastics, and stereolithography (SLA) for resins.',
            'fest2_img': 'fes2-img'

        },
        'section_3': {
            'title_line1': 'SUBTRACTIVE',
            'title_line2': 'MANUFACTURING',
            'text': 'Unlock precision and excellence with our subtractive manufacturing services. Our advanced technologies create parts with impeccable tolerances and exceptional finishes, ensuring your designs come to life flawlessly.',
            'fest4_img': 'fes4-img'

        },
        'section_4': {
            'title_line1': 'COMPOSITE',
            'title_line2': 'MATERIALS',
            'text': 'Our specialists guide material selection and optimization. Whether for aerospace, automotive, or high-performance applications, our services ensure impeccable precision and exceptional surface finishes in advanced components.',
            'fest5_img': 'fes5-img'

        },
        'section_5': {
            'title_line1': 'MATERIALS AND MECHANICAL',
            'title_line2': 'CHARACTERIZATION',
            'text': 'Our experts meticulously analyze materials, from powders to metal components. Our advanced techniques ensure product quality and reliability, preventing future failures and optimizing overall reliability.',
            'fest6_img': 'fes6-img'

        },
        'section_6': {
            'title_line1': 'R&D',
            'title_line2': 'SPECIFIC',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'fest7_img': 'fes7-img'

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
            'title_line1': 'title_line_1',
            'title_line2': 'title_line2',
            'text': 'Description of section 1'
        },
        'section_2': {
            'title_line1': 'Section 2 Title Line 1',
            'title_line2': 'Section 2 Title Line 2',
            'text': 'Description of section 2'
        },
        'section_3': {
            'title_line1': 'Section 3 Title Line 1',
            'title_line2': 'Section 3 Title Line 2',
            'text': 'Description of section 3'
        },
        'section_4': {
            'title_line1': 'Section 4 Title Line 1',
            'title_line2': 'Section 4 Title Line 2',
            'text': 'Description of section 4'
        },
        'section_5': {
            'title_line1': 'Section 5 Title Line 1',
            'title_line2': 'Section 5 Title Line 2',
            'text': 'Description of section 5'
        },
        'section_6': {
            'title_line1': 'Section 6 Title Line 1',
            'title_line2': 'Section 6 Title Line 2',
            'text': 'Description of section 6'
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
            'title_line1': 'Section 1 Title Line 1',
            'title_line2': 'Section 1 Title Line 2',
            'text': 'Description of section 1'
        },
        'section_2': {
            'title_line1': 'Section 2 Title Line 1',
            'title_line2': 'Section 2 Title Line 2',
            'text': 'Description of section 2'
        },
        'section_3': {
            'title_line1': 'Section 3 Title Line 1',
            'title_line2': 'Section 3 Title Line 2',
            'text': 'Description of section 3'
        },
        'section_4': {
            'title_line1': 'Section 4 Title Line 1',
            'title_line2': 'Section 4 Title Line 2',
            'text': 'Description of section 4'
        },
        'section_5': {
            'title_line1': 'Section 5 Title Line 1',
            'title_line2': 'Section 5 Title Line 2',
            'text': 'Description of section 5'
        },
        'section_6': {
            'title_line1': 'Section 6 Title Line 1',
            'title_line2': 'Section 6 Title Line 2',
            'text': 'Description of section 6'
        },
    },
    }
    return render( request ,'platforms/BIO/BIO_services.html',context)
def MSC_services(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': 'Section 1 Title Line 1',
            'title_line2': 'Section 1 Title Line 2',
            'text': 'Description of section 1'
        },
        'section_2': {
            'title_line1': 'Section 2 Title Line 1',
            'title_line2': 'Section 2 Title Line 2',
            'text': 'Description of section 2'
        },
        'section_3': {
            'title_line1': 'Section 3 Title Line 1',
            'title_line2': 'Section 3 Title Line 2',
            'text': 'Description of section 3'
        },
        'section_4': {
            'title_line1': 'Section 4 Title Line 1',
            'title_line2': 'Section 4 Title Line 2',
            'text': 'Description of section 4'
        },
        'section_5': {
            'title_line1': 'Section 5 Title Line 1',
            'title_line2': 'Section 5 Title Line 2',
            'text': 'Description of section 5'
        },
        'section_6': {
            'title_line1': 'Section 6 Title Line 1',
            'title_line2': 'Section 6 Title Line 2',
            'text': 'Description of section 6'
        },
    },
    }
    return render( request ,'platforms/MSC/MSC_services.html',context)
def PCE_services(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': 'Section 1 Title Line 1',
            'title_line2': 'Section 1 Title Line 2',
            'text': 'Description of section 1'
        },
        'section_2': {
            'title_line1': 'Section 2 Title Line 1',
            'title_line2': 'Section 2 Title Line 2',
            'text': 'Description of section 2'
        },
        'section_3': {
            'title_line1': 'Section 3 Title Line 1',
            'title_line2': 'Section 3 Title Line 2',
            'text': 'Description of section 3'
        },
        'section_4': {
            'title_line1': 'Section 4 Title Line 1',
            'title_line2': 'Section 4 Title Line 2',
            'text': 'Description of section 4'
        },
        'section_5': {
            'title_line1': 'Section 5 Title Line 1',
            'title_line2': 'Section 5 Title Line 2',
            'text': 'Description of section 5'
        },
        'section_6': {
            'title_line1': 'Section 6 Title Line 1',
            'title_line2': 'Section 6 Title Line 2',
            'text': 'Description of section 6'
        },
    },
    }
    return render( request ,'platforms/PCE/PCE_services.html',context)
def RESEE_services(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': 'Section 1 Title Line 1',
            'title_line2': 'Section 1 Title Line 2',
            'text': 'Description of section 1'
        },
        'section_2': {
            'title_line1': 'Section 2 Title Line 1',
            'title_line2': 'Section 2 Title Line 2',
            'text': 'Description of section 2'
        },
        'section_3': {
            'title_line1': 'Section 3 Title Line 1',
            'title_line2': 'Section 3 Title Line 2',
            'text': 'Description of section 3'
        },
        'section_4': {
            'title_line1': 'Section 4 Title Line 1',
            'title_line2': 'Section 4 Title Line 2',
            'text': 'Description of section 4'
        },
        'section_5': {
            'title_line1': 'Section 5 Title Line 1',
            'title_line2': 'Section 5 Title Line 2',
            'text': 'Description of section 5'
        },
        'section_6': {
            'title_line1': 'Section 6 Title Line 1',
            'title_line2': 'Section 6 Title Line 2',
            'text': 'Description of section 6'
        },
    },
    }
    return render( request ,'platforms/RESEE/RESEE_services.html',context)
def SAI_services(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        #header
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),

        # Sections
        'sections': {
        'section_1': {
            'title_line1': 'Section 1 Title Line 1',
            'title_line2': 'Section 1 Title Line 2',
            'text': 'Description of section 1'
        },
        'section_2': {
            'title_line1': 'Section 2 Title Line 1',
            'title_line2': 'Section 2 Title Line 2',
            'text': 'Description of section 2'
        },
        'section_3': {
            'title_line1': 'Section 3 Title Line 1',
            'title_line2': 'Section 3 Title Line 2',
            'text': 'Description of section 3'
        },
        'section_4': {
            'title_line1': 'Section 4 Title Line 1',
            'title_line2': 'Section 4 Title Line 2',
            'text': 'Description of section 4'
        },
        'section_5': {
            'title_line1': 'Section 5 Title Line 1',
            'title_line2': 'Section 5 Title Line 2',
            'text': 'Description of section 5'
        },
        'section_6': {
            'title_line1': 'Section 6 Title Line 1',
            'title_line2': 'Section 6 Title Line 2',
            'text': 'Description of section 6'
        },
    },
    }
    return render( request ,'platforms/sai/SAI_services.html',context)


# platforms presentation
def ASMP_index(request):
    context = {
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/FA.mp4",
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
        "video": "../static/video/SSR.mp4",
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
        "video": "../static/video/FA.mp4",
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
        "video": "../static/video/SSR.mp4",
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
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/FA.mp4",
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
        "video": "../static/video/SSR.mp4",
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
        'logo': '../../static/images/logo-white.png',
}

    
    return render( request ,'platforms/MSC/MSC_index.html',context)

def PCE_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/FA.mp4",
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
        "video": "../static/video/SSR.mp4",
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
        "video": "../static/video/FA.mp4",
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
        "video": "../static/video/SSR.mp4",
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
        "video": "../static/video/FA.mp4",
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
        "video": "../static/video/SSR.mp4",
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