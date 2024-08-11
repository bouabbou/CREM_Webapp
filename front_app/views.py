# CREM/views.py
from django.templatetags.static import static

from django.shortcuts import render
from django.urls import reverse


from instrumentation.models import Category, Product


#platfroms infrustructures

def infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
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
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),
        'logo': '../../static/images/logo-grey.png',
    }
    return render(request, 'Infrastructure_FA_EN.html', context)
def BABE_infrastructure(request):
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
       # 'services_url': reverse('BABE_services'),
        'index_url': reverse('BABE_index'),
        'infrastructure_url': reverse('BABE_infrastructure'),
        #'innovation_url': reverse('BABE_innovation'),
        'logo': '../../static/images/logo-grey.png',
        


    }

    return render( request ,'platforms/babe/Infrastructure_FA_EN.html', context)
def MSAC_infrastructure(request):
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
        #'services_url': reverse('MSAC_services'),
        'index_url': reverse('MSAC_index'),
        'infrastructure_url': reverse('MSAC_infrastructure'),
       #'innovation_url': reverse('MSAC_innovation'),
        'logo': '../../static/images/logo-grey.png',
 

    }

    return render( request ,'platforms/msac/MSAC_infrastructure.html', context)
def PEACE_infrastructure(request):
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
        #'services_url': reverse('PEACE_services'),
        'index_url': reverse('PEACE_index'),
        'infrastructure_url': reverse('PEACE_infrastructure'),
        #'innovation_url': reverse('PEACE_innovation'),
        'logo': '../../static/images/logo-grey.png',
 

    }

    return render( request ,'platforms/peace/PEACE_infrastructure.html', context)
def RESAN_infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'image_header': "Image Header",
        'image_descriptions': {
            'part1': "Description Part 1",
            'part2': "resan Part 2",
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
        #'services_url': reverse('RESAN_services'),
        'index_url': reverse('RESAN_index'),
        'infrastructure_url': reverse('RESAN_infrastructure'),
        #'innovation_url': reverse('RESAN_innovation'),
        'logo': '../../static/images/logo-grey.png',



    }

    return render( request ,'platforms/resan/RESAN_infrastructure.html', context)
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
        #'services_url': reverse('SAI_services'),
        'index_url': reverse('SAI_index'),
        'infrastructure_url': reverse('SAI_infrastructure'),
        #'innovation_url': reverse('SAI_innovation'),
        'logo': '../../static/images/logo-grey.png',


    }

    return render( request ,'platforms/sai/SAI_infrastructure.html', context)
def AAD_infrastructure(request):
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
        #'services_url': reverse('AAD_services'),
        'index_url': reverse('AAD_index'),
        'infrastructure_url': reverse('AAD_infrastructure'),
        #'innovation_url': reverse('AAD_innovation'),
        'logo': '../../static/images/logo-grey.png',

    }

    return render( request ,'platforms/aad/AAD_infrastructure.html', context)


def home(request):
    return render( request ,'Home_EN.html')
def contact(request):
    return render( request ,'Contact_EN.html')
def innovation(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),
    }
    return render( request ,'Innovation_FA_EN.html',context)
def services(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),

 
    }
    return render( request ,'Services_FA_EN.html',context)



# platforms presentation
def index(request):
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
        'services_url': reverse('services'),
        'index_url': reverse('index'),
        'infrastructure_url': reverse('infrastructure'),
        'innovation_url': reverse('innovation'),
        'logo': '../../static/images/logo-grey.png',
}

    
    return render( request ,'index_FA_EN.html',context)

def BABE_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/FA.mp4",
        "title": "babe/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM",
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
       
        'index_url': reverse('BABE_index'),
        'infrastructure_url': reverse('BABE_infrastructure'),
        'logo': '../../static/images/logo-grey.png',
}
    return render( request ,'platforms/babe/BABE_index.html', context)

def MSAC_index(request):
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
        #'services_url': reverse('MSAC_services'),
        'index_url': reverse('MSAC_index'),
        'infrastructure_url': reverse('MSAC_infrastructure'),
        #'innovation_url': reverse('MSAC_innovation'),
        'logo': '../../static/images/logo-grey.png',
}

    
    return render( request ,'platforms/msac/MSAC_index.html',context)

def PEACE_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/FA.mp4",
        "title": "PEACE/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM",
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
      #  #'services_url': reverse('PEACE_services'),
        'index_url': reverse('PEACE_index'),
        'infrastructure_url': reverse('PEACE_infrastructure'),
      #  #'innovation_url': reverse('PEACE_innovation'),
        'logo': '../../static/images/logo-grey.png',
}
    return render( request ,'platforms/peace//PEACE_index.html', context)

def RESAN_index(request):
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
        #'services_url': reverse('RESAN_services'),
        'index_url': reverse('RESAN_index'),
        'infrastructure_url': reverse('RESAN_infrastructure'),
        #'innovation_url': reverse('RESAN_innovation'),
        'logo': '../../static/images/logo-grey.png',
}

    
    return render( request ,'platforms/resan/RESAN_index.html',context)

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
        ##'services_url': reverse('SAI_services'),
        'index_url': reverse('SAI_index'),
        'infrastructure_url': reverse('SAI_infrastructure'),
        ##'innovation_url': reverse('SAI_innovation'),
        'logo': '../../static/images/logo-grey.png',
}

    
    return render( request , 'platforms/sai/SAI_index.html',context)

def AAD_index(request):
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
        ##'services_url': reverse('AAD_services'),
        'index_url': reverse('AAD_index'),
        'infrastructure_url': reverse('AAD_infrastructure'),
       # 'innovation_url': reverse('AAD_innovation'),
        'logo': '../../static/images/logo-grey.png',
}

    
    return render( request , 'platforms/aad/AAD_index.html',context)

def presentation(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
    }
    return render( request , 'index_FA_EN.html',context)