# CREM/views.py
from django.templatetags.static import static
from django.views.decorators.cache import cache_page

from django.shortcuts import render
from django.urls import reverse


from instrumentation.models import Category, Machine


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
    products = Machine.objects.all()

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
        'slider_image_url_1': "../static/images/platforms/ASMP/infrastructure_ASMP/flexslider/AMLAB1.png",  
        'slider_image_url_2': "../static/images/platforms/ASMP/infrastructure_ASMP/flexslider/AMLAB2.png", 
        'slider_image_url_3': "../static/images/platforms/ASMP/infrastructure_ASMP/flexslider/AMLAB3.png", 
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
    products = Machine.objects.all()

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
        'slider_image_url_1': "../static/images/flexslider/AMLAB1.png",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB2.png", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.png", 
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
    products = Machine.objects.all()
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
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.png",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.png", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.png",
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
    products = Machine.objects.all()

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
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.png",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.png", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.png",
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
    products = Machine.objects.all()

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
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.png", 
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.png", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.png", 
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
    products = Machine.objects.all()

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
        'slider_image_url_1': "../static/images/flexslider/AMLAB3.png",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB3.png", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.png", 
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
    products = Machine.objects.all()

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
        'platform_name': "AI AND DIGITAL ENGINEERING",
        'slider_image_url_1': "../static/images/flexslider/AMLAB1.png",  
        'slider_image_url_2': "../static/images/flexslider/AMLAB2.png", 
        'slider_image_url_3': "../static/images/flexslider/AMLAB3.png", 
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
                'img': '../static/images/platforms/ASMP/innovation_ASMP/sls.png'

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
                'img': '../static/images/platforms/ASMP/innovation_ASMP/cnc.png'
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
                'img': '../static/images/platforms/ASMP/innovation_ASMP/cm.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
                'img': '../static/images/platforms/ASMP/innovation_ASMP/cf.png'
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
            'title_1': 'Artificial ',
            'title_2': ' INTELLIGENCE',
        },
        'header2': {
            'title_1': 'Virtual ',
            'title_2': ' REALITY',
        },
        'header3': {
            'title_1': 'Collaborative ',
            'title_2': ' ROBOTICS',
        },
        'sections': {
            'section1': {
                'title': 'Deep Learning Algorithms',
                'text': 'Our work in deep learning focuses on developing advanced AI models that can process vast amounts of data to make precise and intelligent decisions. This technology drives innovation across sectors by enabling sophisticated data analysis and predictive modeling.',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section2': {
                'title': 'Natural Language Processing (NLP)',
                'text': 'NLP allows for the creation of AI systems that understand and generate human language. This opens up new possibilities for applications such as chatbots, automated translations, and sentiment analysis, enhancing user interactions and experiences. ',
                'img': '../static/images/Innovation/sls.png'

            },
            'section3': {
                'title': 'Computer Vision',
                'text': 'Computer vision technology enables machines to interpret and understand visual information from the world. Our expertise in computer vision facilitates applications such as facial recognition, object detection, and automated quality inspection in manufacturing. ',
                'img': '../static/images/Innovation/FDM.png'

            },
            
            'section5': {
                'title': 'Immersive Training Programs',
                'text': 'We develop VR training programs that provide realistic and engaging learning experiences. These programs are used in various industries, including healthcare, automotive, and manufacturing, to enhance skills and safety. ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'Interactive Simulations',
                'text': 'Our interactive simulations create virtual environments where users can explore and interact with digital models. This technology is particularly useful for design, prototyping, and educational purposes, allowing for detailed visualization and experimentation. ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'Robotic Assistance Using Humanoids',
                'text': 'We specialize in developing humanoid robots that provide assistance in various settings, such as healthcare, customer service, and domestic environments. These humanoids are designed to interact naturally with humans, performing tasks that enhance daily living and improve quality of life.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'Mobile Robotics',
                'text': 'Our expertise includes developing algorithms for mobile robotics, enabling robots to navigate and operate autonomously in diverse environments. These mobile robots are used in applications ranging from logistics and warehouse management to exploration and surveillance.',
                'img': '../static/images/Innovation/CF.png'
            },
            'section9': {
                'title': 'Aerial Robotics',
                'text': 'We focus on the navigation of drones in complex spaces, developing advanced algorithms to ensure precise and safe operation. These aerial robots are utilized in applications such as surveillance, environmental monitoring, and delivery services.',
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
            'title_1': 'Solar ',
            'title_2': ' Energies',
        },
        'header2': {
            'title_1': 'Energy ',
            'title_2': ' Storage',
        },
        'header3': {
            'title_1': 'Desalination ',
            'title_2': ' Technologies',
        },
        'header4': {
            'title_1': 'Energy ',
            'title_2': ' Efficiency',
        },
        'sections': {
            'section1': {
                'title': 'Solar Technologiescial',
                'tag': '',
                'text': 'Our research into PV technology covers a broad spectrum of essential aspects. These include enhancing system performance, assessing the durability of new materials, predicting system performance, integrating PV systems into the power grid, and analyzing the economic and policy implications of PV power. We also focus on enhancing thermal solar technologies through advanced modeling, material innovation, cost optimization, and environmental assessment.',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section5': {
                'title': 'Batteries',
                'tag': '',
                'text': 'We specialize in developing innovative, cost-effective battery solutions. Our work encompasses designing, building, and testing battery systems while optimizing their economic performance and minimizing environmental impact.',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'Desalination',
                'tag': '',
                'text': 'Our research focuses on developing innovative and cost-effective desalination solutions. We address industry challenges by creating new materials, components and technologies. Our research involves designing, building, and testing desalination systems that integrate renewable energy sources with advanced membrane processes like Reverse Osmosis (RO), Forward Osmosis (FO), and Membrane Distillation (MD).',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'Buildings',
                'tag': '',
                'text': 'We specialize in sustainable building solutions, combining bio-based and recycled materials with innovative smart home technologies. Our expertise extends to building energy management, where we develop predictive models to optimize energy consumption.',
                'img': '../static/images/Innovation/TP.png'
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
                'text': 'Our work in Laser Powder Bed Fusion (LPBF) centers on producing precise metal components. LPBF allows for intricate and customized geometries, enabling limitless innovation, especially in high-demand industries.',
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
                'text': 'This technology efficiently produces thermoplastic parts. Suitable for both conceptual prototypes and functional components. Our work with FDM aims to optimize this popular 3D printing process. ',
                'img': '../static/images/Innovation/FDM.png'

            },
            'section4': {
                'title': 'STEREOLITHOGRAPHY',
                'tag': 'SLA',
                'text': "Stereolithography (SLA) is resin-based 3D printing technologies with unparalleled precision. it's used for custom dental prosthetics, detailed designs or any high-precision part. ",
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
            'title_1': '',
            'title_2': '',
        },
        'header2': {
            'title_1': '',
            'title_2': '',
        },
        'sections': {
            'section1': {
                'title': 'NMR: A Revolution in AgriFood Research',
                'tag': '',
                'text': 'We developed a novel NMR technique that employs spatially selective chemical shift filters, adiabatic pulses, and TOCSY to accurately quantify carbohydrates. This method eliminates background interference and the need for calibration curves, providing high precision with low detection limits and making it suitable for routine analysis of various natural matrices.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno_msc01.png'
            },
            'section2': {
                'title': 'NMR Insights into DES-Based Catalysis',
                'tag': '',
                'text': 'We work on using NMR spectroscopy to investigate catalytic reactions in Deep Eutectic Solvents (DESs), aiming to uncover reaction mechanisms, identify intermediates, and optimize catalytic performance. This work supports green chemistry by advancing the use of environmentally friendly solvents and promoting sustainable catalytic processes.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno_msc2.png'

            },
            'section3': {
                'title': 'A Powerful Tool for Drug Innovation',
                'tag': '',
                'text': 'We developed an NMR-based method to screen covalent inhibitors of cysteine proteases, including the SARS-CoV-2 main protease (M pro). Using real-time NMR spectroscopy, we tracked S-C bond formation and reaction kinetics with various Michael acceptors. This approach links chemical reactivity to inhibitory activity, enhancing drug discovery for antiviral agents targeting cysteine proteases.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno3.jpg'

            },
            'section4': {
                'title': 'NMR-Enabled High-Throughput Screening of Plant Metabolites',
                'tag': '',
                'text': 'High-resolution NMR has become essential in plant metabolism research. We’ve developed novel NMR-based methods tailored to screen, identify, and quantify metabolites in plant extracts, focusing on CBD and THC in Moroccan cannabis. These advanced techniques enable precise and efficient cannabis analysis, supporting scientific research, medicinal quality control, and cosmetic product development.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno4.jpg'

            },
            'section5': {
                'title': 'Enhancing Biomarker Detection in Blood Serum Using Advanced NMR Techniques',
                'tag': '',
                'text': 'We work on improving early disease diagnosis by optimizing Nuclear Magnetic Resonance (NMR) techniques for detecting biomarkers in blood serum. This research aims to refine NMR protocols to achieve greater sensitivity and accuracy in identifying biomarkers for cancer and metabolic disorders, ultimately advancing diagnostic methods and clinical applications.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno5.png'
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
            'title_1': 'Geotechnical ',
        },
        'header2': {
            'title_1': 'Concrete ',
        },
        'header3': {
            'title_1': 'Traffic ',
            'title_2': ' Facilities',
            'style': 'background-color: white;'
        },
        'sections': {
            'section1': {
                'title': 'Geotechnical characterization',
                'text': 'We employ advanced geotechnical testing methods to better understand soil and rock behavior for infrastructure design and construction.',
                'img': '../static/images/Innovation/lpbf.png'
            },
            'section5': {
                'title': 'Advanced materials testing',
                'text': 'We investigate the properties and behavior of innovative materials such as high-performance concrete, sustainable composites, and recycled materials.-Structural health monitoring: We develop and apply cutting-edge techniques to assess the condition and performance of structures throughout their lifecycle. ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section6': {
                'title': 'Structural health monitoring',
                'text': 'We develop and apply cutting-edge techniques to assess the condition and performance of structures throughout their lifecycle. ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'Innovative Asphalt Technologies',
                'text': 'Pioneering the development of high-performance asphalt mixtures that are long-lasting, weather-resistant, and environmentally friendly.',
                'img': '../static/images/Innovation/TP.png'
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
                'text1': 'text text tex tetx tetx tetsx ',
                'img': '../static/images/Innovation/CNC.png'
            },
            'section7': {
                'title': 'THERMOPLASTIC',
                'tag': 'COMPOSITES',
                'text1': 'Thermoplastic composites offer a balance of lightness and strength, making them ideal for aerospace, automotive, and other industrial applications.',
                'img': '../static/images/Innovation/TP.png'
            },
            'section8': {
                'title': 'CARBON FIBER',
                'tag': 'COMPOSITES',
                'text1': 'Exceptionally strong, carbon fiber composites find use in structural components, including high-end automotive vehicles and advanced sports equipment.',
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
            'img': '../../static/images/platforms/ASMP/services_ASMP/cao.png'
            
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
            'img': '../../static/images/platforms/ASMP/services_ASMP/cnc_srv.png'

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
            'title_line1': 'Advanced',
            'title_line2': 'Chatbots',
            'text': ' Tailor-made design of advanced chatbots to automate customer interactions, improve online support, and boost business operational efficiency. ',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'Character',
            'title_line2': 'Recognition Systems',
            'text': ' Design of OCR systems to efficiently extract and interpret text data from printed or handwritten documents. These systems are used to digitize documents, automate data management and improve information retrieval processes.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'Facial',
            'title_line2': 'Recognition Systems',
            'text': 'Creating advanced algorithms for facial recognition. These algorithms are deployed in applications for security, access control, workforce management, and even personalized user experiences.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'Event',
            'title_line2': 'Deployment',
            'text': 'Robot deployment services for special events, trade fairs, exhibitions or product launches.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'Customer Service',
            'title_line2': 'And Marketing',
            'text': 'Use robots to improve customer service by providing information, answering questions and collecting feedback. Robots can also be used for interactive marketing campaigns.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'Health',
            'title_line2': 'And Wellness',
            'text': 'Proposing solutions for healthcare facilities, using robots to entertain patients, encourage physical activity, or provide medical reminders.',
            'img': '../../static/images/Serv/7.jpeg'

        },
        'section_5': {
            'title_line1': 'Custom Content',
            'title_line2': 'Development',
            'text': 'Create interactive content tailored to customers needs, such as games, presentations, dialogs and animations.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'Virtual',
            'title_line2': 'And Augmented Reality',
            'text': 'Develop virtual and augmented reality content; Train in the use of the following equipment: HTC vive pro eye VR headset, Base stations, Controllers',
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
            'title_line1': 'BIOMEDICAL ',
            'title_line2': 'INSTRUMENTATION',
            'text': '•	Computer-aided design and manufacturing of biomedical instruments creating precise parts and prototypes with advanced CAD/CAE software',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'Cellular ',
            'title_line2': 'and Molecular Analyses',
            'text': '',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'Recombinant ',
            'title_line2': 'Protein Production',
            'text': 'Gene cloning and optimization in various vectors, including cloning, expression, and multigenic vectors. Production in heterologous systems and optimization of bio-production conditions. Protein purification and crystallization. Packaging of protein preparations.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'Cell Culture ',
            'title_line2': 'Testing',
            'text': 'In vitro tests: cell migration & invasion, proliferation, viability, adhesion, and real-time cellular and molecular analysis. Measurement of cellular cytotoxicity for organic molecules. Determination of antimicrobial activities (antibacterial, antifungal, etc.). Optimization of cell culture and molecular screening conditions.',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'Molecular ',
            'title_line2': 'Diagnostics',
            'text': 'Design of primers and probes for identifying and characterizing bacterial, fungal, and viral pathogens (including COVID-19) using PCR, RT-PCR, and real-time PCR. Sample preparation, including RNA extraction and long DNA fragment extraction. Construction of genomic libraries. DNA sequencing.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'Biochemical Analysis of Food ',
            'title_line2': 'and Environmental Samples',
            'text': 'Quantification of key organic molecules (amino acids, sugars, lipids, proteins, etc.). Quantification of biological activities.',
            'img': '../../static/images/Serv/7.jpeg'

        },
        'section_7': {
            'title_line1': 'Proteomic ',
            'title_line2': 'Analyses',
            'text': 'Protein detection through immunoblotting, immunoprecipitation, and peptide/protein quality control. Protein quantification using Western blot, ELISA, electrophoresis, and other methods.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_8': {
            'title_line1': 'Microbiological ',
            'title_line2': 'Analyses',
            'text': '',
            'img': '../../static/images/Serv/7.jpeg'

        },
        'section_9': {
            'title_line1': 'Food and Environmental ',
            'title_line2': 'Product Testing',
            'text': 'Detection and identification of pathogenic microorganisms. Serotyping of foodborne pathogens. Identification of hygiene and quality indicator microorganisms. Audits and control of cleaning-disinfection operations (surface, air, and hood control). Microbiological quality control of various water types.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_10': {
            'title_line1': 'Pharmaceutical and Cosmetic ',
            'title_line2': 'Product Testing',
            'text': 'Detection, enumeration, and identification of pathogenic microorganisms (bacteria, yeasts, fungi, viruses). Verification of antimicrobial efficacy. Bacteriological testing of finished products.',
            'img': '../../static/images/Serv/7.jpeg'

        },
        'section_11': {
            'title_line1': 'Optimization of Biochemical/Biological ',
            'title_line2': 'Processes',
            'text': 'Immobilization and optimization of biocatalysts (cellular and enzymatic). Scaling up of biochemical processes (fermentation and enzymatic catalysis).',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_12': {
            'title_line1': 'Spectroscopic Elucidation of ',
            'title_line2': 'Organic/Biological Molecules',
            'text': 'Separation and spectrometric analysis. Spectroscopic analyses: HPLC-MS/MS, GC-MS, NMR, FT-IR, XRD, UV-NIR.',
            'img': '../../static/images/Serv/7.jpeg'

        },
        'section_13': {
            'title_line1': 'Continuous ',
            'title_line2': 'Training',
            'text': 'Our platform offers comprehensive continuous training programs designed to keep professionals up-to-date with the latest advancements and techniques. We provide tailored workshops and courses to enhance skills and knowledge, ensuring your team remains at the forefront of the industry.',
            'img': '../../static/images/Serv/5.jpg'

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
            'title_line1': 'Advanced Spectroscopic',
            'title_line2': 'Analysis',
            'text': 'Our Advanced Spectroscopy Solutions deliver comprehensive chemical analysis, including structural elucidation, accurate quantitative measurements, insights into molecular interactions, observation of dynamic behavior, and detailed material characterization.',
            'img': '../../static/images/platforms/MSC/services_msc/srv1.jpg'
            
        },
        'section_2': {
            'title_line1': 'XRD Services for ',
            'title_line2': 'Materials Science',
            'text': 'Our platform offers extensive XRD services for materials characterization, supporting process optimization and development. Services include phase and structure determination, nanomaterial analysis, phase transformation observation, and characterization of thin films and nanostructured layers.',
            'img': '../../static/images/platforms/MSC/services_msc/srv2.jpg'

        },
        'section_3': {
            'title_line1': 'Thermal ',
            'title_line2': 'Analysis',
            'text': 'Our platform offers advanced thermal analysis with TGA and DSC, offering detailed insights into material properties for research, development, and quality control. TGA covers decomposition, volatile content, residue analysis, and stability, while DSC includes melting temperatures, glass transitions, crystallization, and thermal reactions.',
            'img': '../../static/images/platforms/MSC/services_msc/srv3.jpg'

        },
        'section_4': {
            'title_line1': 'D-SEM & Acoustic ',
            'title_line2': 'Microscopy',
            'text': 'Our platform offers advanced material characterization with state-of-the-art SEM and Acoustic Microscopy. SEM services include high-resolution imaging, elemental analysis, and topographic mapping. Acoustic Microscopy services provide density mapping, defect detection, and 3D imaging for non-destructive material examination.',
            'img': '../../static/images/platforms/MSC/services_msc/srv4.jpg'

        },
        'section_5': {
            'title_line1': 'E-DMA/TMA ',
            'title_line2': 'Analysis',
            'text': 'Our platform offers DMA and TMA services for in-depth material characterization. DMA services include measuring elastic modulus, glass transition temperature (Tg), and viscoelastic properties. TMA services cover thermal expansion, temperature-dependent deformation, and viscoelastic behavior under thermal load.',
            'img': '../../static/images/platforms/MSC/services_msc/srv5.jpg'

        },
        'section_6': {
            'title_line1': 'Rheology and Viscosity ',
            'title_line2': 'Analysis',
            'text': 'Our rheology service offers detailed analysis of fluids, semi-solids, and solids, including viscosity measurement, viscoelastic structure analysis, and shear behavior. We help optimize formulations and enhance product quality for pharmaceuticals, cosmetics, polymers, and food.',
            'img': '../../static/images/platforms/MSC/services_msc/srv6.jpg'

        },
        'section_7': {
            'title_line1': 'Surface and Porosity Characterization ',
            'title_line2': '',
            'text': 'Utilizing the BET method, our Surface and Porosity Characterization service measures specific surface areas and pore characteristics. This analysis is crucial for understanding material performance in industrial, pharmaceutical, and environmental applications, aiding in the design and optimization of advanced materials.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_8': {
            'title_line1': 'Supporting ',
            'title_line2': 'R&D',
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
            'title_line1': 'ANALYSES OF SOILS AND CONSTRUCTION MATERIALS',
            'title_line2': '',
            'text': '-Estimation of Atterberg limits: limits of elasticity and plasticity - Calculation of the sand equivalent - Calculation of the particle size distribution of a soil - Estimation of the fracturing resistance of aggregates (Los Angeles) - Estimation of the friction resistance of aggregates (micro-Deval)  - Compression tests for mortar and concrete',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'Lanes',
            'title_line2': '',
            'text': '-Aging of bitumen at RTFOT - Calculation of the dynamic stability of asphalt-based road pavement structures using rutting tests.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'Non-destructive testing',
            'title_line2': '',
            'text': 'Determination of the resistance of concrete: By measuring the speed of propagation of ultrasound in concrete, we can estimate its compressive resistance. -Internal defect detection: Identification of voids, cracks and other structural defects in concrete. -Evaluation of concrete homogeneity: Verification of the consistency and uniformity of the concrete. -Assessment of the condition of existing structures: Detection of damage, cracks and corrosion of reinforced concrete.',
            'img': '../../static/images/Serv/4.jpeg'

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
            'title_line1': 'Solar Energy Solutions',
            'title_line2': '',
            'text': 'We specialize in evaluating the performance of photovoltaic and concentrating solar systems. Our services encompass a comprehensive approach to assessing system efficiency, environmental impact, and economic viability. Core Competencies: Performance Assessment, Environmental Impact Analysis, Economic Evaluation, Reliability and Durability Testing, Predictive Modeling',
            'img': '../../static/images/Serv/1.png'
            
        },
        'section_2': {
            'title_line1': 'PV Material Development and Validation',
            'title_line2': '',
            'text': 'Our cutting-edge solar simulator provides a controlled environment for comprehensive testing of photovoltaic materials. Key Services: Rigorous Material Evaluation: Accurately assess the performance of new photovoltaic materials under simulated solar conditions. Industry Standard Compliance: Ensure that materials meet stringent industry requirements and certifications.',
            'img': '../../static/images/Serv/2.jpeg'

        },
        'section_3': {
            'title_line1': 'Energy Storage Solutions',
            'title_line2': '',
            'text': 'Our storage research center is equipped with state-of-the-art facilities for comprehensive evaluation of energy storage technologies. Key Services: VRFB Component Characterization: In-depth analysis of membrane, electrolyte, electrode, and bipolar plate components for vanadium redox flow batteries (VRFBs). Battery Performance Testing: Advanced battery testing to assess capacity, internal resistance, temperature, and lifespan of VRFBs and other battery technologies.',
            'img': '../../static/images/Serv/4.jpeg'

        },
        'section_4': {
            'title_line1': 'Advanced Desalination solutions',
            'title_line2': '',
            'text': 'Our desalination platform is dedicated to enhancing the efficiency and performance of Forward Osmosis (FO), Reverse Osmosis (RO), and Pressure Retarded Osmosis (PRO) desalination systems. Key Services: Membrane Performance Evaluation, System Optimization, Solution Analysis, Precise Osmolarity Measurement',
            'img': '../../static/images/Serv/6.jpg'

        },
        'section_5': {
            'title_line1': 'Thermal Analysis',
            'title_line2': '',
            'text': 'We provide thermal characterization and optimization services for thermodynamics and heat transfer applications.',
            'img': '../../static/images/Serv/5.jpg'

        },
        'section_6': {
            'title_line1': 'Research Consulting',
            'title_line2': '',
            'text': 'We provide expert guidance on research methodology, design, and analysis. We team up with other CREM platform to develop and produce components or prototypes for energy systems or desalination processes, and to perform sample characterization.',
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
        "image": "../static/images/platforms/ASMP/index_ASMP/3S_AM.png",
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
        "title": "BIOTECHNOLOGY AND BIOMEDICAL ENGINEERING",
        "description": "Innovate. Collaborate. Transform."
    },
    "about": {
        "text_1": "Welcome to our Biotechnology and Biomedical Engineering Platform, a hub for research, services, and training. We utilize the latest advancements in microbiology, cell biology, molecular biology, chemistry, and engineering to drive innovation and share expertise. Our mission is to create groundbreaking solutions for partners in health, agri-food, environmental, cosmetic, and agronomy sectors. Collaborate with us to pioneer progress in these critical fields.",
        "text_2": "We specialize in protein engineering, recombinant DNA technologies, and post-transcriptional RNA modification linked to diseases. Our services include developing medical devices, synthesizing nanomaterials for medical use, and conducting microbiological analyses in the agri-food, environmental, pharmaceutical, and cosmetic sectors."
    },
    "third_section": {
        "title": "Biotechnology example",
        "description": "Lorem ipsum",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Lorem ipsum",
            "description": "Lorem ipsum"
        },
        "point_2": {
            "title": "Lorem ipsum",
            "description": "Lorem ipsum"
        },
        "point_3": {
            "title": "Lorem ipsum",
            "description": "Lorem ipsum"
        },
        "point_4": {
            "title": "Lorem ipsum",
            "description": "Lorem ipsum"
        }
    },
    "video": {
        "title_l": "Bio/Substractive",
        "title_r": "MANUFACTURING",
        "video": "../static/video/BIO.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "",
        "tab_1": {
            "header": "Lorem ipsum",
            "title": "Lorem ipsum",
            "description": "Lorem ipsum",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Lorem ipsum",
            "title": "Lorem ipsum",
            "description": "Lorem ipsum",
           
        },
        "tab_3": {
            "header": "Lorem ipsum",
            "title": "Lorem ipsum",
            "description": "Lorem ipsum",
           
        },
        "tab_4": {
            "header": "Lorem ipsum",
            "title": "Lorem ipsum",
            "description": "Lorem ipsum"
          
        }
        ,
         "tab_4": {
            "header": "test",
            "title": "test",
            "description": "test"
          
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
        "title": "Materials, Synthesis, and Characterization",
        "description": "Platforms for Innovation, Solutions in Synthesis, Results through Characterization.",
    },
    "about": {
        "text_1": "At the forefront of material characterization, our platform integrates cutting-edge technology to offer precise and reliable measurements across a broad spectrum of applications. Our mission is to drive innovation through advanced instrumentation and software solutions, enabling researchers and industries to push the boundaries of material science. Our dedication to innovation extends beyond our instruments.",
        "text_2": "At our characterization platform, we provide unmatched support and expertise to help you navigate the complexities of material characterization across diverse application areas, including material science, pharmaceuticals, agroalimentary, chemistry, and polymers. Our skilled team is dedicated to delivering precise insights and solutions tailored to your needs, ensuring optimal performance and innovation in your projects."
    },
    "third_section": {
        "title": "Advantages of using our characterization platform:",
        "description": "",
        "image": "../static/images/platforms/MSC/index_MSC/sec3.png",
        "point_1": {
            "title": "Diverse Analytical Tools:",
            "description": "Access to a comprehensive suite of cutting-edge instruments, tailored to support a wide range of research needs with flexibility and precision."
        },
        "point_2": {
            "title": "Industrial precision:",
            "description": "Benefit from advanced tools and expertise designed for high-accuracy industrial analysis, ideal for both occasional and regular needs."
        },
        "point_3": {
            "title": "Customizable Services:",
            "description": "Utilize on-demand, customizable services to get exactly what you need, when you need it, enhancing research efficiency and adaptability."
        },
        "point_4": {
            "title": "Expert Interpretation:",
            "description": "Receive detailed and insightful analysis from a team of specialists in chemistry, mechanics, and physics, ensuring clear understanding and actionable results."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/MSC.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Impact on Research and Industry",
        "description": "",
        "tab_1": {
            "header": "Materials Science",
            "title": "Revolutionizing High-Performance Materials",
            "description": "Advanced materials enable the development of high-performance materials for electronics, aerospace, and energy sectors, while performance optimization analyzes thermal and mechanical properties to ensure material reliability.",
        },
        "tab_2": {
            "header": "Biotechnology and Medicine",
            "title": "Innovations in Biomaterials and Drug Development",
            "description": "Biomaterials provide insights into the molecular structure of biological materials, enhancing implants and drug delivery systems. Drug development optimizes formulations and interactions through detailed analysis.",
           
        },
        "tab_3": {
            "header": "Industrial Processes",
            "title": "Enhancing Efficiency and Sustainability",
            "description": "Catalyst optimization enhances efficiency and sustainability in chemical manufacturing, while process improvement reduces waste and streamlines operations through comprehensive material analysis.",
           
        },
        "tab_4": {
            "header": "Environmental and Sustainability",
            "title": "Advancing Environmental Protection",
            "description": "Pollution monitoring analyzes pollutants and supports environmental protection efforts, while sustainable materials aid in developing eco-friendly materials and processes."
          
        },
        "tab_5": {
            "header": "Food and Agriculture",
            "title": "Ensuring Quality and Innovation",
            "description": "Quality control ensures food quality by detecting contaminants and verifying composition, while agricultural innovations improve practices and crop yields through material analysis.",
           
        },
        "tab_6": {
            "header": "Energy Sector",
            "title": "Driving Sustainable Energy Solutions",
            "description": "Pollution monitoring analyzes pollutants and supports environmental protection efforts, while sustainable materials aid in developing eco-friendly materials and processes.",
           
        },
        "tab_7": {
            "header": "",
            "title": "",
            "description": ""
          
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
        "description": "Civil Engineering solutions for a better world"
    },
    "about": {
        "text_1": "Our team of experts partners with clients to deliver exceptional geotechnical, concrete, and pavement engineering services, ensuring precise solutions for critical company needs.",
        "text_2": "Our team boasts extensive expertise in geotechnical, concrete, and pavement engineering, providing innovative solutions for challenging projects."
    },
    "third_section": {
        "title": "State-of-the-Art Solutions for Engineering Challenges",
        "description": "Our civil engineering lab delivers precise testing and analysis with cutting-edge equipment and expert professionals, ensuring reliable results and innovative solutions for your projects.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Expertise and Experience",
            "description": "Our laboratory boasts a team of highly skilled engineers and technicians with extensive experience in the field. This expertise ensures accurate and reliable results for all your testing and analysis needs."
        },
        "point_2": {
            "title": "State-of-the-art-equipment",
            "description": "We are equipped with the latest testing equipment and technology, allowing us to conduct comprehensive and precise investigations. Our advanced facilities enable us to handle a wide range of projects with efficiency and accuracy."
        },
        "point_3": {
            "title": "Customized Solutions",
            "description": "We understand that every project is unique. Our laboratory offers tailored testing and analysis services to meet your specific requirements, providing you with the data needed to make informed decisions."
        },
        "point_4": {
            "title": "Commitment to Quality",
            "description": "We adhere to strict quality control standards and ensuring the highest level of accuracy and reliability in our results."
        }
    },
    "video": {
        "title_l": "ADDITIVE",
        "title_r": "MANUFACTURING",
        "video": "../static/video/PCE.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Empowering Innovation in Civil Engineering",
        "tab_1": {
            "header": "Geotechnics",
            "title": "Soil Characterization and Analysis",
            "description": "Advanced soil analysis methodologies to optimize the design and construction of foundations and Providing innovative solutions to complex geotechnical problems through cutting-edge research and development.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Traffic facilities",
            "title": " Asphalt Mixture Evaluation ",
            "description": "Advanced bitumen analysis machines streamline the process of evaluating bitumen properties, ensuring the construction of durable and reliable road pavements. These machines automate various testing procedures, reducing human error and improving efficiency. They provide accurate data on bitumen's characteristics, aiding in informed decision-making for road design and maintenance.",
           
        },
        "tab_3": {
            "header": "Non-destructuve testing",
            "title": "Structural Health Monitoring ",
            "description": "Implement state-of-the-art non-destructive testing techniques to assess structural integrity and Provide accurate and reliable condition assessment reports for informed decision-making.",
           
        }
    },
     #header : 
      #  'services_url': reverse('PCE_services'),
        'index_url': reverse('PCE_index'),
        'infrastructure_url': reverse('PCE_infrastructure'),
        'innovation_url': reverse('PCE_innovation'),
        'services_url': reverse('PCE_services'),
        'logo': '../../static/images/logo-white.png',
}
    return render( request ,'platforms/PCE//PCE_index.html', context)

def RESEE_index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 
        
        "header": {
        "video": "../static/video/RESEE.mp4",
        "title": "",
        "description": ""
    },
    "about": {
        "text_1": "Our platform is a comprehensive resource equipped with state-of-the-art design, manufacturing, and characterization tools for developing sustainable energy solutions. It fosters innovation and research in key areas such as renewable energies, energy storage, and energy efficiency.",
        "text_2": "We advance renewable energy, storage, and efficiency technologies by designing innovative solutions for harnessing, storing, and optimizing energy. We also test and develop advanced tools to evaluate renewable energy systems, thermal systems, and batteries, ensuring they meet specifications and support sustainability goals. Our Open-Air Laboratories offer real-world testing and insights into energy-efficient technologies."
    },
    "third_section": {
        "title": "Renewable Energies Advantages",
        "description": "Renewable energies offer numerous benefits over traditional fossil fuels. These advantages contribute to a more sustainable and environmentally friendly future.",
        "image": "../static/images/fes7.jpg",
        "point_1": {
            "title": "Durability",
            "description": "Renewable energy sources are inexhaustible; their use guarantees a constant source of energy for future generations without disrupting the availability of resources for future needs."
        },
        "point_2": {
            "title": "Environmental-Friendly",
            "description": "Renewable energy sources cut greenhouse gas emissions more than fossil fuels, aiding in climate change mitigation and improving air quality, which benefits public health."
        },
        "point_3": {
            "title": "Long-term cost savings",
            "description": "Renewable energy technologies often lead to lower operational costs compared to fossil fuels."
        },
        "point_4": {
            "title": "Increased energy access",
            "description": "Renewable energy technologies can provide electricity to remote and underserved areas, improving living conditions and quality of life."
        }
    },
    "video": {
        "title_l": "ENERGY",
        "title_r": "ENGINEERING",
        "video": "../static/video/RESEE.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "",
        "tab_1": {
            "header": "Renewable Energy",
            "title": "",
            "description": "Pioneering cutting-edge solutions for harnessing renewable energy technologies for both connected and off-grid environments. Design and implement advanced technologies for clean hydrogen generation. Advancing energy storage capabilities with innovative technologies like Vanadium Redox Flow Batteries. Building a sustainable energy future through technological breakthroughs.",

            "img_before": "../static/images/static-media/Turbine1.jpg",
            "img_after": "../static/images/static-media/Turbine2.jpg"
        },
        "tab_2": {
            "header": "Manufacturing",
            "title": "",
            "description": "Innovative energy-efficient solutions to streamline manufacturing processes, reduce operational costs, and minimize environmental impact. Optimize energy consumption across the manufacturing value chain to lower costs, increase competitiveness, and achieve sustainability goals. Implement new methods for industrial decarbonization.",
           
        },
        "tab_3": {
            "header": "Buildings",
            "title": "",
            "description": "Develop innovative building envelopes and insulation systems. Implement energy-efficient building practices to reduce environmental impact and enhance occupant comfort. Development and integration of smart home technologies to optimize energy consumption.",
           
        },
        "tab_4": {
            "header": "Desalination",
            "title": "",
            "description": "Drive advancements in desalination processes to provide clean water sources. Explore innovative approaches for large-scale, low-cost water desalination."
          
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
        "title_l": "DIGITAL",
        "title_r": "ENGINEERING",
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