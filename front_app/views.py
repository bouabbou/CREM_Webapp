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
                'title': "CNC Machinning",
                'subtitle': "Substractive Manufacturing",
            },
            'section_2': {
                'title': "Fused deposition modeling",
                'subtitle': "Additive Manufacturing",
            },
            'section_3': {
                'title': "Powder-Based",
                'subtitle': "Additive Manufacturing",
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
        'image_header': "Advanced characterization",
        'image_descriptions': {
            'part1': "Materials",
            'part2': "Synthesis",
            'part3': "Testing",
            'part4': "Characterization",
        },
        'header_img': "../static/images/platforms/MSC/infrastructure_MSC/MSC_header.png",
        'gallery_texts': {
            'section_1': {
                'title': "Nuclear Magnetic Resonance",
                'subtitle': "NMR Laboratory",
            },
            'section_2': {
                'title': "Microscopy",
                'subtitle': "Laboratory",
            },
            'section_3': {
                'title': "X-Ray Crystallography",
                'subtitle': "XRD Laboratory",
            },
        },
        'platform_name': "Materials, Synthesis, and Characterization Platform",
        'slider_image_url_1': "../static/images/platforms/MSC/infrastructure_MSC/lab01.webp",  
        'slider_image_url_2': "../static/images/platforms/MSC/infrastructure_MSC/lab02.webp", 
        'slider_image_url_3': "../static/images/platforms/MSC/infrastructure_MSC/lab03.webp",
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
        'image_header': "Civil Engineering",
        'image_descriptions': {
            'part1': "Civil Engineering",
            'part2': "Traffic Facilities",
            'part3': "Geotechnics",
            'part4': "Cement-Matrix Structures",
        },
        'header_img': "../static/images/platforms/PCE/infrastructure_PCE/PCE_header.jpg",
        'gallery_texts': {
            'section_1': {
                'title': "Cement-Matrix Structures",
                'subtitle': "Laboratory",
            },
            'section_2': {
                'title': "Geotechnics",
                'subtitle': "Laboratory",
            },
            'section_3': {
                'title': "Traffic Facilities",
                'subtitle': "Laboratory",
            },
        },
        'platform_name': "PROCESS ENGINEERING AND CIVIL ENGINEERING",
        'slider_image_url_1': "../static/images/platforms/PCE/infrastructure_PCE/lab01.webp", 
        'slider_image_url_2': "../static/images/platforms/PCE/infrastructure_PCE/lab02.webp", 
        'slider_image_url_3': "../static/images/platforms/PCE/infrastructure_PCE/lab03.webp", 
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
        'image_header': "Energy Engineering",
        'image_descriptions': {
            'part1': "Renewable energy and Storage",
            'part2': "Thermodynamic systems",
            'part3': "Desalination",
            
        },
        'header_img': "../static/images/platforms/RESEE/infrastructure_RESEE/RESEE_header.webp",
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
        'platform_name': "RENEWABLE ENERGY, STORAGE AND ENERGY EFFICIENCY",
        'slider_image_url_1': "../static/images/platforms/RESEE/infrastructure_RESEE/lab01.webp", 
        'slider_image_url_2': "../static/images/platforms/RESEE/infrastructure_RESEE/lab02.webp", 
        'slider_image_url_3': "../static/images/platforms/RESEE/infrastructure_RESEE/lab03.webp", 
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
        'image_header': "Advanced AI and Digital engineering",
        'image_descriptions': {
            'part1': "AI",
            'part2': "Digital Engineering",
            'part3': "Virtual Reality",
            'part4': "Robotics and Cobotics",
        },
        'header_img': "../static/images/platforms/AIDE/infrastructure_AIDE/AIDE_header.png",
        'gallery_texts': {
             'section_1': {
                'title': "Virtual reality",
                'subtitle': "Laboratory",
            },
            'section_2': {
                'title': "Robotics and Cobotics",
                'subtitle': "Laboratory",
            },
            'section_3': {
                'title': "AI and Digital engineering",
                'subtitle': "Laboratory",
            },
        },
        'platform_name': "AI AND DIGITAL ENGINEERING",
        'slider_image_url_1': "../static/images/platforms/AIDE/infrastructure_AIDE/lab01.webp",  
        'slider_image_url_2': "../static/images/platforms/AIDE/infrastructure_AIDE/lab02.webp", 
        'slider_image_url_3': "../static/images/platforms/AIDE/infrastructure_AIDE/lab03.webp", 
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
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno1.jpg'
            },
            'section2': {
                'title': 'Natural Language Processing (NLP)',
                'text': 'NLP allows for the creation of AI systems that understand and generate human language. This opens up new possibilities for applications such as chatbots, automated translations, and sentiment analysis, enhancing user interactions and experiences. ',
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno2.jpg'

            },
            'section3': {
                'title': 'Computer Vision',
                'text': 'Computer vision technology enables machines to interpret and understand visual information from the world. Our expertise in computer vision facilitates applications such as facial recognition, object detection, and automated quality inspection in manufacturing. ',
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno3.jpg'

            },
            
            'section4': {
                'title': 'Immersive Training Programs',
                'text': 'We develop VR training programs that provide realistic and engaging learning experiences. These programs are used in various industries, including healthcare, automotive, and manufacturing, to enhance skills and safety. ',
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno4.jpg'
            },
            'section5': {
                'title': 'Interactive Simulations',
                'text': 'Our interactive simulations create virtual environments where users can explore and interact with digital models. This technology is particularly useful for design, prototyping, and educational purposes, allowing for detailed visualization and experimentation. ',
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno5.jpg'
            },
            'section6': {
                'title': 'Robotic Assistance Using Humanoids',
                'text': 'We specialize in developing humanoid robots that provide assistance in various settings, such as healthcare, customer service, and domestic environments. These humanoids are designed to interact naturally with humans, performing tasks that enhance daily living and improve quality of life.',
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno6.jpg'
            },
            'section7': {
                'title': 'Mobile Robotics',
                'text': 'Our expertise includes developing algorithms for mobile robotics, enabling robots to navigate and operate autonomously in diverse environments. These mobile robots are used in applications ranging from logistics and warehouse management to exploration and surveillance.',
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno8.png'
            },
            'section8': {
                'title': 'Aerial Robotics',
                'text': 'We focus on the navigation of drones in complex spaces, developing advanced algorithms to ensure precise and safe operation. These aerial robots are utilized in applications such as surveillance, environmental monitoring, and delivery services.',
                'img': '../static/images/platforms/AIDE/innovation_AIDE/inno8.jpg'
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
                'title': 'Concentrated Solar Power',
                'tag': '',
                'text': 'At the forefront of concentrating solar power (CSP) research, we focus on advancing technology through cutting-edge modeling, material breakthroughs, cost optimization, and comprehensive environmental assessments. Our work aims to improve efficiency and sustainability in CSP systems.',
                'img': '../static/images/platforms/RESEE/innovation_RESEE/inno1.jpg'
            },
            'section2': {
                'title': 'Photovoltaics',
                'tag': '',
                'text': 'Our research in PV technology focuses on improving system performance, assessing material durability, predicting output, optimizing grid integration, and analyzing economic and policy impacts.',
                'img': '../static/images/platforms/RESEE/innovation_RESEE/inno2.jpg'
            },
            'section3': {
                'title': 'Hydrogen Production',
                'tag': '',
                'text': 'We innovate in cost-effective hydrogen production through the water splitting process, designing, building, and testing new components. Our approach incorporates custom electrodes and metal 3D-printed parts for improved efficiency.',
                'img': '../static/images/platforms/RESEE/innovation_RESEE/inno3.jpg'
            },
            'section4': {
                'title': 'Redox Flow Batteries',
                'tag': '',
                'text': 'We specialize in developing innovative, cost-effective battery solutions. Our expertise spans the entire lifecycle, from design and manufacturing to testing and optimization, with a strong focus on economic viability and environmental sustainability. ',
                'img': '../static/images/platforms/RESEE/innovation_RESEE/inno4.jpg'
            },
            'section5': {
                'title': 'Redox Flow Batteries',
                'tag': '',
                'text': 'We specialize in developing innovative, cost-effective battery solutions. Our expertise spans the entire lifecycle, from design and manufacturing to testing and optimization, with a strong focus on economic viability and environmental sustainability. ',
                'img': '../static/images/platforms/RESEE/innovation_RESEE/inno5.jpg'
            },
            'section6': {
                'title': 'Desalination',
                'tag': '',
                'text': 'Our research focuses on developing innovative and cost-effective desalination solutions. We address industry challenges by creating new materials, components and technologies. Our research involves designing, building, and testing desalination systems that integrate renewable energy sources with advanced membrane processes like Reverse Osmosis (RO), Forward Osmosis (FO), and Membrane Distillation (MD).',
                'img': '../static/images/platforms/RESEE/innovation_RESEE/inno3.jpg'
            },
            'section7': {
                'title': 'Buildings',
                'tag': '',
                'text': 'We specialize in sustainable building solutions, combining bio-based and recycled materials with innovative smart home technologies. Our expertise extends to building energy management, where we develop predictive models to optimize energy consumption.',
                'img': '../static/images/platforms/RESEE/innovation_RESEE/inno7.png'
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
            'title_1': 'Cutting-Edge ',
            'title_2': ' R&D',
        },
        'header2': {
            'title_1': 'ADVANCED ANALYTICAL',
            'title_2': ' TECHNIQUES',
        },
        'header3': {
            'title_1': 'DIAGNOSTICS AND',
            'title_2': ' EDUCATIONAL INNOVATION',
        },
        'sections': {
            'section1': {
                'title': 'Advanced Drug Discovery',
                'tag': '',
                'text': 'Our Medicinal Chemistry Laboratory is pioneering new methods in drug discovery, utilizing AI-driven algorithms to design and synthesize novel pharmaceutical compounds. This approach accelerates the identification of potential drug candidates, reducing the time and cost associated with traditional drug development processes.',
                'img': '../static/images/platforms/BIO/innovation_BIO/inno1.jpg'
            },
            'section2': {
                'title': 'Genetic Engineering Breakthroughs',
                'tag': '',
                'text': 'In the Biotechnology Laboratory, researchers are making significant strides in genetic engineering. By employing CRISPR-Cas9 technology, they are able to precisely edit genes, leading to advancements in gene therapy, agricultural biotechnology, and the development of genetically modified organisms (GMOs) with enhanced traits.',
                'img': '../static/images/platforms/BIO/innovation_BIO/inno2.jpg'

            },
            'section3': {
                'title': 'Innovative Medical Devices',
                'tag': '',
                'text': 'The Biomedical Instrumentation Laboratory is at the forefront of developing cutting-edge medical devices. Recent projects include the creation of wearable health monitors that provide real-time data on vital signs, enabling early detection and management of chronic diseases.',
                'img': '../static/images/platforms/BIO/innovation_BIO/inno3.jpg'

            },
            'section4': {
                'title': 'Environmental Monitoring',
                'tag': '',
                'text': 'Utilizing Gas Chromatography-Mass Spectrometry (GC-MS), our team is conducting innovative research in environmental monitoring. This technology enables the precise detection and analysis of pollutants, contributing to efforts in environmental protection and sustainability.',
                'img': '../static/images/platforms/BIO/innovation_BIO/inno4.jpg'

            },
            'section5': {
                'title': 'High-Resolution Imaging',
                'tag': '',
                'text': 'Our platform’s advanced fluorescence microscopy capabilities allow for high-resolution imaging of biological samples. This technology is crucial for studying cellular processes in detail, leading to a better understanding of disease mechanisms and the development of targeted therapies.',
                'img': '../static/images/platforms/BIO/innovation_BIO/inno5.jpg'
            },
            'section6': {
                'title': 'Protein Purification Techniques',
                'tag': '',
                'text': 'Researchers in our Biotechnology Laboratory are refining protein purification techniques using Fast Protein Liquid Chromatography (FPLC). These advancements are essential for producing high-purity proteins for use in pharmaceuticals, diagnostics, and research applications.',
                'img': '../static/images/platforms/BIO/innovation_BIO/inno6.jpg'
            },
            'section7': {
                'title': 'Molecular Diagnostics',
                'tag': '',
                'text': 'Our Molecular Diagnostics services are enhancing the detection and characterization of pathogens. By developing advanced PCR-based assays, we are improving the accuracy and speed of diagnosing infectious diseases, including emerging viral threats.',
                'img': '../static/images/platforms/BIO/innovation_BIO/inno7.jpg'
            },
            'section8': {
                'title': 'Continuous Training Programs',
                'tag': '',
                'text': 'We offer comprehensive continuous training programs to keep researchers and industry professionals updated with the latest advancements in biotechnology and biomedical engineering. These programs ensure that our partners are equipped with the knowledge and skills needed to drive innovation in their respective fields.',
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
                'title': 'A Revolution in AgriFood Research',
                'tag': '',
                'text': 'We developed a novel NMR approach for complex matrices, integrating spatially selective chemical shift filters, adiabatic pulses, and TOCSY. This method eliminates background interference and the need for calibration curves, providing high precision and making it well-suited for routine analysis of diverse natural samples.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno1.jpg'
            },
            'section2': {
                'title': 'NMR Insights into DES-Based Catalysis',
                'tag': '',
                'text': 'Explore catalytic reactions in Deep Eutectic Solvents (DESs) to investigate reaction mechanisms, identify intermediates, and improve catalytic performance. This research advances green chemistry by supporting the use of environmentally friendly solvents and fostering sustainable catalytic processes.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno2.jpg'

            },
            'section3': {
                'title': 'A Powerful Tool for Drug Innovation',
                'tag': '',
                'text': 'We developed an NMR-based method to screen covalent inhibitors of proteases, connecting chemical reactivity with inhibitory activity. This approach represents a significant advancement in drug discovery for protease-targeting agents.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno3.jpg'

            },
            'section4': {
                'title': 'NMR-Enabled High-Throughput Screening of Plant Metabolites',
                'tag': '',
                'text': 'Our ongoing research focuses on developing advanced NMR-based methods to screen, identify, and quantify metabolites in plant extracts. These innovative techniques support cutting-edge research, ensure rigorous quality control, and drive the development of high-value products.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno4.jpg'

            },
            'section5': {
                'title': 'Enhancing Biomarker Detection in Blood Serum',
                'tag': '',
                'text': 'We focus on enhancing early disease diagnosis by optimizing NMR techniques to detect biomarkers in blood serum. Our research aims to improve sensitivity and accuracy in identifying biomarkers for cancer and metabolic disorders, advancing diagnostic methods and clinical applications.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno5.jpg'
            },
            'section6': {
                'title': 'Solid-State NMR for Characterizing Biomaterials',
                'tag': '',
                'text': 'We explore solid-state NMR for characterizing biomaterials, focusing on selecting suitable materials for tissue regeneration. We investigate their potential for biomineralization and examine their surface properties for various applications.',
                'img': '../static/images/platforms/MSC/innovation_MSC/inno6.jpg'
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
            'title_1': 'Non-Destructive ',
            'title_2': 'Testing',

        },
        'header2': {
            'title_1': 'Construction and Asphalt ',
            'title_2': 'Technologies',

        },
        'header3': {
            'title_1': 'Geotechnics ',
            'title_2': '',
            'style': 'background-color: white;'
        },
        'sections': {
            'section1': {
                'title': 'Radiography',
                'text': 'Radiography utilizes X-rays or gamma rays to penetrate materials and create images of internal structures. This technique enables the detection of defects such as cracks, porosity, and inclusions, providing valuable insights into material integrity and assembly quality.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno1.png'
            },
            'section2': {
                'title': 'Eddy currents (ECT)',
                'text': 'ECT method utilizes electromagnetic induction to detect surface defects and variations in conductivity within conductive materials. By inducing eddy currents in the material and measuring their response, ECT can identify anomalies such as cracks, corrosion, and material defects. This technique is widely used in various industries, including aerospace, automotive, and power generation. ',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno2.png'
            },
            'section3': {
                'title': 'Magnetic particle inspection (MPI)',
                'text': 'MPI method is used to detect surface and subsurface defects in ferromagnetic materials. By applying a magnetic field to the material and then applying magnetic particles, any discontinuities or defects will attract the particles, making them visible for inspection.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno3.png'
            },
            'section4': {
                'title': 'Ultrasonics Testing',
                'text': 'Ultrasonics Testing is a non-destructive testing method that utilizes high-frequency sound waves to detect internal defects within materials.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno4.png'
            },
            'section5': {
                'title': 'Liquid penetrant inspection (LPT)',
                'text': 'LPT is a non-destructive testing method used to detect surface-breaking defects in materials. By applying a penetrant liquid to the surface, allowing it to penetrate into any cracks or discontinuities, and then revealing the penetrant using a developer, LPT can effectively identify defects that may not be visible to the naked eye.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno5.png'
            },
            'section6': {
                'title': 'Bitumen modification',
                'text': 'Advanced bitumen analysis focuses on developing innovative additives and polymers to enhance bitumen properties, understanding their molecular interactions, and evaluating the long-term performance of modified bitumen in asphalt mixtures.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno6.jpg'
            },
            'section7': {
                'title': '3D construction printing ',
                'text': 'This technology revolutionizes the construction industry by enabling the manufactruring of complex structures with unprecedented precision, reduced material waste and energy efficiency. Our 3D printing machines, such as the 3D Potter and the CyBe RC, are driving innovation in this field.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno7.jpg'
            },
            'section8': {
                'title': 'Numerical soil modeling',
                'text': 'Development of numerical models to simulate in situ soil behavior like finite element modeling, discrete element modeling and limit equilibrium methods.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno8.png'
            },
            'section9': {
                'title': 'Soil-structure interaction',
                'text': 'Numerical and experimental analysis of the interactions between structures and soils, particularly under cyclic loading conditions such as earthquakes and traffic.',
                'img': '../static/images/platforms/PCE/innovation_PCE/inno9.png'
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
            'title_1': 'Sensor Technologies',
            'title_2': '',
        },
        'header2': {
            'title_1': 'Data Acquisition',
            'title_2': '',
        },
        'header3': {
            'title_1': 'Data Processing',
            'title_2': '',
        },
        'header4': {
            'title_1': 'Simulation and Modeling',
            'title_2': '',
        },
        'header5': {
            'title_1': 'Calibration',
            'title_2': '',
        },
        'sections': {
            'section1': {
                'title': 'Laser-based Sensors',
                'tag': '',
                'text': 'Our work in laser-based sensors focuses on achieving high-precision measurements for a variety of applications. This technology allows for non-contact detection of physical parameters such as distance, speed, and surface characteristics, providing accurate data for industrial automation, aerospace, and more.',
                'img': '../static/images/platforms/sai/innovation_sai/inno1.jpg'
            },
            'section2': {
                'title': 'Optical Sensors',
                'tag': '',
                'text': 'Optical sensors utilize light-based technologies to measure parameters such as light intensity, color, and displacement. These sensors are ideal for applications requiring high sensitivity and accuracy, including environmental monitoring, quality control, and healthcare diagnostics.',
                'img': '../static/images/platforms/sai/innovation_sai/inno2.jpg'
            },
            'section3': {
                'title': 'Electrochemical Sensors',
                'tag': '',
                'text': 'Electrochemical sensors are employed to detect and measure chemical substances and concentrations. They are crucial for applications in environmental monitoring, medical diagnostics, and industrial process control, providing reliable and real-time data.',
                'img': '../static/images/platforms/sai/innovation_sai/inno3.jpg'
            },
            'section4': {
                'title': 'Acoustic Sensors',
                'tag': '',
                'text': 'Acoustic sensors use sound waves to detect and measure various parameters such as distance, velocity, and material properties. This technology is applied in fields such as automotive safety systems, industrial inspection, and environmental studies.',
                'img': '../static/images/platforms/sai/innovation_sai/inno4.jpg'
            },
            'section5': {
                'title': 'Embedded Systems',
                'tag': '',
                'text': 'We integrate advanced embedded systems for efficient data acquisition from various sensors. These systems manage real-time data collection and processing, ensuring accurate and reliable information for further analysis.',
                'img': '../static/images/platforms/sai/innovation_sai/inno5.jpg'
            },
            'section6': {
                'title': 'Data Integration and Management',
                'tag': '',
                'text': 'Our platform utilizes sophisticated methods for integrating and managing sensor data. This includes filtering, analyzing, and presenting data to support informed decision-making and enhance system performance.',
                'img': '../static/images/platforms/sai/innovation_sai/inno6.jpg'
            },
            'section7': {
                'title': 'Signal Processing',
                'tag': '',
                'text': 'Our solutions involve advanced signal processing techniques to enhance the quality and accuracy of sensor data. This includes noise reduction, signal amplification, and data smoothing to ensure precise measurements.',
                'img': '../static/images/platforms/sai/innovation_sai/inno7.jpg'
            },
            'section8': {
                'title': 'Analog-to-Digital Conversion',
                'tag': '',
                'text': 'We provide conversion services for transforming data between analog and digital formats, facilitating better integration and usability of sensor data in various applications.',
                'img': '../static/images/platforms/sai/innovation_sai/inno8.jpg'
            },
            'section9': {
                'title': 'System Simulation',
                'tag': '',
                'text': 'We use simulation tools such as LabVIEW and MATLAB to model and test sensor systems. This helps in designing accurate and effective solutions, predicting performance, and optimizing system integration.',
                'img': '../static/images/platforms/sai/innovation_sai/inno9.jpg'
            },
            'section10': {
                'title': 'Sensor Calibration',
                'tag': '',
                'text': 'We offer comprehensive calibration services for mechatronic sensors, ensuring they meet the highest standards of accuracy and reliability. Our calibration processes are designed to enhance sensor performance and maintain consistency in measurements.',
                'img': '../static/images/platforms/sai/innovation_sai/inno10.jpg'
            }
        },
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 
        'services_url': reverse('SAI_services'),
        'index_url': reverse('SAI_index'),
        'infrastructure_url': reverse('SAI_infrastructure'),
        'innovation_url': reverse('SAI_innovation'),
    }
    return render(request, 'platforms/sai/SAI_innovation.html', context)


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
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv1.png'
            
        },
        'section_2': {
            'title_line1': 'Character',
            'title_line2': 'Recognition Systems',
            'text': ' Design of OCR systems to efficiently extract and interpret text data from printed or handwritten documents. These systems are used to digitize documents, automate data management and improve information retrieval processes.',
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv2.jpg'

        },
        'section_3': {
            'title_line1': 'Facial',
            'title_line2': 'Recognition Systems',
            'text': 'Creating advanced algorithms for facial recognition. These algorithms are deployed in applications for security, access control, workforce management, and even personalized user experiences.',
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv3.png'

        },
        'section_4': {
            'title_line1': 'Event',
            'title_line2': 'Deployment',
            'text': 'Robot deployment services for special events, trade fairs, exhibitions or product launches.',
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv4.jpg'
            

        },
        'section_5': {
            'title_line1': 'Customer Service',
            'title_line2': 'And Marketing',
            'text': 'Use robots to improve customer service by providing information, answering questions and collecting feedback. Robots can also be used for interactive marketing campaigns.',
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv5.jpg'

        },
        'section_6': {
            'title_line1': 'Health',
            'title_line2': 'And Wellness',
            'text': 'Proposing solutions for healthcare facilities, using robots to entertain patients, encourage physical activity, or provide medical reminders.',
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv6.jpg'

        },
        'section_7': {
            'title_line1': 'Custom Content',
            'title_line2': 'Development',
            'text': 'Create interactive content tailored to customers needs, such as games, presentations, dialogs and animations.',
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv7.jpg'

        },
        'section_8': {
            'title_line1': 'Virtual',
            'title_line2': 'And Augmented Reality',
            'text': 'Develop virtual and augmented reality content; Train in the use of the following equipment: HTC vive pro eye VR headset, Base stations, Controllers',
            'img': '../../static/images/platforms/AIDE/services_AIDE/srv8.jpg'

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
        'title_line1': 'Biomedical ',
        'title_line2': 'Instrumentation',
        'text': 'We offer computer-aided design and manufacturing of biomedical instruments, creating precise parts and prototypes with advanced CAD/CAE software.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv1.jpg'
    },
    'section_2': {
        'title_line1': 'Optimization of ',
        'title_line2': 'Biochemical/Biological Processes',
        'text': 'We specialize in the immobilization and optimization of biocatalysts (cellular and enzymatic) and scaling up of biochemical processes (fermentation and enzymatic catalysis).',
        'img': '../../static/images/platforms/BIO/services_BIO/srv2.jpg'
    },
    'section_3': {
        'title_line1': 'Recombinant ',
        'title_line2': 'Protein Production',
        'text': 'Our services include gene cloning and optimization in various vectors, production in heterologous systems, optimization of bio-production conditions, protein purification, crystallization, and packaging of protein preparations.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv3.jpg'
    },
    'section_4': {
        'title_line1': 'Cell Culture ',
        'title_line2': 'Testing',
        'text': 'We conduct in vitro tests for cell migration, invasion, proliferation, viability, adhesion, and real-time cellular and molecular analysis. Additionally, we measure cellular cytotoxicity for organic molecules, determine antimicrobial activities, and optimize cell culture and molecular screening conditions.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv4.jpg'
    },
    'section_5': {
        'title_line1': 'Molecular ',
        'title_line2': 'Diagnostics',
        'text': 'We design primers and probes for identifying and characterizing bacterial, fungal, and viral pathogens (including COVID-19) using PCR, RT-PCR, and real-time PCR. Our services also include sample preparation, genomic library construction, and DNA sequencing.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv5.jpg'
    },
    'section_6': {
        'title_line1': 'Biochemical Analysis ',
        'title_line2': 'of Food and Environmental Samples',
        'text': 'We quantify key organic molecules (amino acids, sugars, lipids, proteins, etc.) and biological activities in food and environmental samples.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv6.jpg'
    },
    'section_7': {
        'title_line1': 'Proteomic ',
        'title_line2': 'Analyses',
        'text': 'Our proteomic services include protein detection through immunoblotting, immunoprecipitation, and peptide/protein quality control, as well as protein quantification using Western blot, ELISA, electrophoresis, and other methods.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv7.jpg'
    },
    'section_8': {
        'title_line1': 'Microbiological ',
        'title_line2': 'Analyses',
        'text': 'We offer detection and identification of pathogenic microorganisms, serotyping of foodborne pathogens, identification of hygiene and quality indicator microorganisms, audits and control of cleaning-disinfection operations, and microbiological quality control of various water types.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv8.jpg'
    },
    'section_9': {
        'title_line1': 'Pharmaceutical and ',
        'title_line2': 'Cosmetic Product Testing',
        'text': 'Our testing services include detection, enumeration, and identification of pathogenic microorganisms (bacteria, yeasts, fungi, viruses), verification of antimicrobial efficacy, and bacteriological testing of finished products.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv9.jpg'
    },
    'section_10': {
        'title_line1': 'Spectroscopic Elucidation ',
        'title_line2': 'of Organic/Biological Molecules',
        'text': 'Our services include separation and spectrometric analysis, as well as spectroscopic analyses using HPLC-MS/MS, GC-MS, NMR, FT-IR, XRD, and UV-NIR.',
        'img': '../../static/images/platforms/BIO/services_BIO/srv10.jpg'
    }
}
 
    
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
            'img':'../static/images/platforms/MSC/services_MSC/srv1.jpg'
            
        },
        'section_2': {
            'title_line1': 'XRD Services for ',
            'title_line2': 'Materials Science',
            'text': 'Our platform offers extensive XRD services for materials characterization, supporting process optimization and development. Services include phase and structure determination, nanomaterial analysis, phase transformation observation, and characterization of thin films and nanostructured layers.',
            'img': '../static/images/platforms/MSC/services_MSC/srv2.jpg'

        },
        'section_3': {
            'title_line1': 'Thermal ',
            'title_line2': 'Analysis',
            'text': 'Our platform offers advanced thermal analysis with TGA and DSC, offering detailed insights into material properties for research, development, and quality control. TGA covers decomposition, volatile content, residue analysis, and stability, while DSC includes melting temperatures, glass transitions, crystallization, and thermal reactions.',
            'img': '../static/images/platforms/MSC/services_MSC/srv3.jpg'

        },
        'section_4': {
            'title_line1': 'D-SEM & Acoustic ',
            'title_line2': 'Microscopy',
            'text': 'Our platform offers advanced material characterization with state-of-the-art SEM and Acoustic Microscopy. SEM services include high-resolution imaging, elemental analysis, and topographic mapping. Acoustic Microscopy services provide density mapping, defect detection, and 3D imaging for non-destructive material examination.',
            'img': '../static/images/platforms/MSC/services_MSC/srv4.jpg'

        },
        'section_5': {
            'title_line1': 'E-DMA/TMA ',
            'title_line2': 'Analysis',
            'text': 'Our platform offers DMA and TMA services for in-depth material characterization. DMA services include measuring elastic modulus, glass transition temperature (Tg), and viscoelastic properties. TMA services cover thermal expansion, temperature-dependent deformation, and viscoelastic behavior under thermal load.',
            'img': '../static/images/platforms/MSC/services_MSC/srv5.jpg'

        },
        'section_6': {
            'title_line1': 'Rheology and Viscosity ',
            'title_line2': 'Analysis',
            'text': 'Our rheology service offers detailed analysis of fluids, semi-solids, and solids, including viscosity measurement, viscoelastic structure analysis, and shear behavior. We help optimize formulations and enhance product quality for pharmaceuticals, cosmetics, polymers, and food.',
            'img': '../static/images/platforms/MSC/services_MSC/srv6.jpg'

        },
        'section_7': {
            'title_line1': 'Surface and Porosity Characterization ',
            'title_line2': '',
            'text': 'Utilizing the BET method, our Surface and Porosity Characterization service measures specific surface areas and pore characteristics. This analysis is crucial for understanding material performance in industrial, pharmaceutical, and environmental applications, aiding in the design and optimization of advanced materials.',
            'img': '../static/images/platforms/MSC/services_MSC/srv7.jpg'

        },
        'section_8': {
            'title_line1': 'Supporting ',
            'title_line2': 'R&D',
            'text': 'Partner with our dedicated research and development team. We thrive on challenges, turning your innovative ideas into reality. Explore our full range of services and let’s create something extraordinary together.',
            'img': '../static/images/platforms/MSC/services_MSC/srv8.jpg'

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
            'img': '../static/images/platforms/PCE/services_PCE/serv1.jpg'
            
        },
        'section_2': {
            'title_line1': 'Lanes',
            'title_line2': '',
            'text': '-Aging of bitumen at RTFOT - Calculation of the dynamic stability of asphalt-based road pavement structures using rutting tests.',
            'img': '../static/images/platforms/PCE/services_PCE/serv2.webp'

        },
        'section_3': {
            'title_line1': 'Non-destructive testing',
            'title_line2': '',
            'text': 'Determination of the resistance of concrete: By measuring the speed of propagation of ultrasound in concrete, we can estimate its compressive resistance. -Internal defect detection: Identification of voids, cracks and other structural defects in concrete. -Evaluation of concrete homogeneity: Verification of the consistency and uniformity of the concrete. -Assessment of the condition of existing structures: Detection of damage, cracks and corrosion of reinforced concrete.',
            'img': '../static/images/platforms/PCE/services_PCE/serv3.jpg'

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
            'img': '../static/images/platforms/RESEE/services_RESEE/srv1.jpg'
            
        },
        'section_2': {
            'title_line1': 'PV Material Development and Validation',
            'title_line2': '',
            'text': 'Our cutting-edge solar simulator provides a controlled environment for comprehensive testing of photovoltaic materials. Key Services: Rigorous Material Evaluation: Accurately assess the performance of new photovoltaic materials under simulated solar conditions. Industry Standard Compliance: Ensure that materials meet stringent industry requirements and certifications.',
            'img': '../static/images/platforms/RESEE/services_RESEE/srv2.jpg'

        },
        'section_3': {
            'title_line1': 'Energy Storage Solutions',
            'title_line2': '',
            'text': 'Our storage research center is equipped with state-of-the-art facilities for comprehensive evaluation of energy storage technologies. Key Services: VRFB Component Characterization: In-depth analysis of membrane, electrolyte, electrode, and bipolar plate components for vanadium redox flow batteries (VRFBs). Battery Performance Testing: Advanced battery testing to assess capacity, internal resistance, temperature, and lifespan of VRFBs and other battery technologies.',
            'img': '../static/images/platforms/RESEE/services_RESEE/srv3.jpg'

        },
        'section_4': {
            'title_line1': 'Advanced Desalination solutions',
            'title_line2': '',
            'text': 'Our desalination platform is dedicated to enhancing the efficiency and performance of Forward Osmosis (FO), Reverse Osmosis (RO), and Pressure Retarded Osmosis (PRO) desalination systems. Key Services: Membrane Performance Evaluation, System Optimization, Solution Analysis, Precise Osmolarity Measurement',
            'img': '../static/images/platforms/RESEE/services_RESEE/srv4.jpg'

        },
        'section_5': {
            'title_line1': 'Thermal Analysis',
            'title_line2': '',
            'text': 'We provide thermal characterization and optimization services for thermodynamics and heat transfer applications.',
            'img': '../static/images/platforms/RESEE/services_RESEE/srv5.jpg'

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
            'title_line1': 'DETECTION',
            'title_line2': '',
            'text': 'We specialize in detecting and collecting physical parameters for various domains, including healthcare (vital signs, diagnostics, wearable devices), agriculture (soil moisture, crop health, environmental conditions), automotive (vehicle performance, engine diagnostics, safety systems), and aerospace (flight control, engine monitoring, structural health). We also offer tailored solutions for other specialized fields.',
            'img': '../static/images/platforms/sai/services_sai/srv1.jpg'
        },
        'section_2': {
            'title_line1': 'DATA',
            'title_line2': 'ACQUISITION',
            'text': 'We use various electronic and embedded systems to acquire data and integrate it into the acquisition chain. This includes selecting and implementing the right hardware to ensure accurate and reliable data capture.',
            'img': '../static/images/platforms/sai/services_sai/srv2.jpg'
        },
        'section_3': {
            'title_line1': 'DATA',
            'title_line2': 'PROCESSING',
            'text': 'Our data processing solutions utilize electronic components for efficient signal processing and data handling, converting data between analog and digital formats, and amplifying signals to ensure accurate measurements and readings.',
            'img': '../static/images/platforms/sai/services_sai/srv3.jpg'
        },
        'section_4': {
            'title_line1': 'SIMULATION',
            'title_line2': '',
            'text': 'We employ simulation and modeling tools such as LabVIEW and MATLAB to design and test systems. These tools help in developing accurate models and simulations of sensor systems and their interactions.',
            'img': '../static/images/platforms/sai/services_sai/srv4.jpg'
        },
        'section_5': {
            'title_line1': 'OTHER',
            'title_line2': 'SERVICES',
            'text': 'We provide calibration services for mechatronic sensors to ensure they perform with the highest accuracy and reliability. This includes fine-tuning sensors to meet specific application requirements and standards.',
            'img': '../static/images/Serv/7.jpeg'
        },
    },
    }
    
    return render(request, 'platforms/sai/SAI_services.html', context)



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
        "title_l": "BIO",
        "title_r": "TECHNOLOGY",
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
        "title_l": "MATERIALS",
        "title_r": "SCIENCE",
        "video": "../static/video/MSC2.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Impact on Research and Industry",
        "description": "",
        "tab_1": {
            "header": "Materials Science",
            "title": " Materials research and Advanced Characterization for Cutting-Edge Industries ",
            "description": "Advanced characterization techniques are employed to optimize material performance across cutting-edge industries such as electronics, aerospace, and energy, driving innovation and ensuring reliability in high-demand applications.",
        },
        "tab_2": {
            "header": "Biotechnology and Medicine",
            "title": "Advancing Biomaterials and Drug Development",
            "description": "Biomaterials offer insights into the molecular structure of biological materials. Through new formulations and detailed analysis of interactions, the drug development process is optimized, leading to the creation of innovative implants and drug delivery systems.",
           
        },
        "tab_3": {
            "header": "Industrial Processes",
            "title": "Boosting Industrial Efficiency Via Analysis",
            "description": "Industrial efficiency is enhanced through precise material analysis, optimizing performance, improving quality, and promoting sustainability across processes.",
           
        },
        "tab_4": {
            "header": "Environmental and Sustainability",
            "title": "Advancing Environmental Protection",
            "description": "Pollution monitoring enables effective pollutant detection and supports environmental protection efforts, complemented by a sustainable approach that fosters the development of eco-friendly materials and processes."
          
        },
        "tab_5": {
            "header": "Food and Agriculture",
            "title": "Advanced Analysis For Quality, Safety and Authenticity",
            "description": "Materials synthesis and characterization are essential in the food and agriculture industry, ensuring product quality, safety, and authenticity through precise composition analysis, contaminant detection, and process optimization.",
           
        },
        "tab_6": {
            "header": "Energy Sector",
            "title": "Energy Storage Materials",
            "description": "Advanced characterization and testing techniques are essential for enhancing the performance, durability, and efficiency of energy storage materials, enabling breakthroughs in applications such as batteries, supercapacitors, and energy systems.",
           
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
        "image": "../static/images/platforms/PCE/index_PCE/section3.jpg",
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
        "title_l": "CIVIL",
        "title_r": "ENGINEERING",
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
        "title": "Energy systems and process engineering",
        "description": "For a cleaner future"
    },
    "about": {
        "text_1": "Our platform is a comprehensive resource equipped with state-of-the-art design, manufacturing, and characterization tools for developing sustainable energy solutions. It fosters innovation and research in key areas such as renewable energies, energy storage, and energy efficiency.",
        "text_2": "We advance renewable energy, storage, and efficiency technologies by designing innovative solutions for harnessing, storing, and optimizing energy. We also test and develop advanced tools to evaluate renewable energy systems, thermal systems, and batteries, ensuring they meet specifications and support sustainability goals. Our Open-Air Laboratories offer real-world testing and insights into energy-efficient technologies."
    },
    "third_section": {
        "title": "Renewable Energies Advantages",
        "description": "Renewable energies offer numerous benefits over traditional fossil fuels. These advantages contribute to a more sustainable and environmentally friendly future.",
        "image": "../static/images/platforms/RESEE/index_RESEE/section3.jpg",
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
        "title": "Sensors and Instrumentation Platform",
        "description": "Precision technology, innovative sensors, and reliable instrumentation in one place"
    },
    "about": {
        "text_1": "Our Sensors and Instrumentation Platform plays a pivotal role in the SMART FACTORY initiative, providing cutting-edge capabilities for sensor development and calibration essential to data acquisition. By collaborating with all Euromed research platforms, it drives innovation and supports advanced research across a range of applications.",
        "text_2": "Our platform specializes in advanced sensor technologies, offering end-to-end solutions from design and prototyping to testing and implementation. Leveraging cutting-edge materials and methods, we deliver high-precision sensors and reliable systems for industrial automation, environmental monitoring, healthcare, and beyond."
    },
    "third_section": {
        "title": "The critical role of sensor technology",
        "description": "Sensor technology encompasses a wide range of devices, enabling automation, real-time monitoring, and data-driven decision-making. Here are the key roles:",
        "image": "../static/images/platforms/sai/index_sai/section3.jpg",
        "point_1": {
            "title": "Predictive Maintenance & Asset Management",
            "description": "Vibration and thermal sensors detect early signs of equipment failure. While AI-driven analytics predict maintenance needs, improving efficiency and longevity."
        },
        "point_2": {
            "title": "Automation & Smart Manufacturing 4.0",
            "description": "IoT-enabled sensors integrate with robotics and AI systems to enable autonomous production and enhances precision in manufacturing."
        },
        "point_3": {
            "title": "Quality Control & Process Optimization",
            "description": "Sensors inspect products in real-time, detecting defects and ensuring consistent quality. It improves material usage, reducing waste and enhancing sustainability."
        },
        "point_4": {
            "title": "Supply Chain & Logistics Optimization",
            "description": "RFID, GPS, and environmental sensors track goods, improving logistics and inventory management. It ensures real-time visibility and minimizes disruptions."
        }
    },
    "video": {
        "title_l": "SENSOR",
        "title_r": "TECHNOLOGY",
        "video": "../static/video/SAI.mp4",
        "bg_img" : "../static/images/play.png"
    },
    "details_section": {
        "title": "Driving Innovation Across Industries",
        "description": "At the Sensors and Instrumentation Platform, we harness cutting-edge technologies to advance progress and innovation across diverse industrial sectors:",
        "tab_1": {
            "header": "Aerospace",
            "title": "Precision and Reliability",
            "description": "In the aerospace industry, our advanced sensor technologies enable the precise monitoring and control of critical systems. From flight control systems to engine diagnostics, our sensors enhance safety, performance, and efficiency.",

        },
        "tab_2": {
            "header": "Automotive",
            "title": "Smart and Efficient",
            "description": "Our sensors contribute to the development of smart, efficient, and safe vehicles. They are integral to systems such as adaptive cruise control, collision detection, and engine performance monitoring, driving the evolution of next-generation automotive technologies.",
           
        },
        "tab_3": {
            "header": "Medical Technology",
            "title": "Innovative Healthcare Solutions",
            "description": " In the medical field, our sensors provide accurate and real-time monitoring of vital signs and medical conditions. They are essential for developing advanced diagnostic devices, wearable health monitors, and smart medical implants, improving patient care and treatment outcomes.",
           
        },
        "tab_4": {
            "header": "Environmental Monitoring",
            "title": "Sustainable Solutions",
            "description": "Our sensors play a crucial role in environmental monitoring, offering precise measurement of air and water quality, weather conditions, and pollution levels. These sensors support the development of sustainable solutions for environmental protection and climate change mitigation."
          
        },
        "tab_5": {
            "header": "Industrial Automation",
            "title": "Enhanced Productivity",
            "description": "In industrial automation, our sensors ensure accurate monitoring and control of manufacturing processes. They enable predictive maintenance, quality control, and efficient resource management, driving productivity and innovation in smart factories.",
           
        },
        "tab_6": {
            "header": "Infrastructure and Smart Cities",
            "title": "Building the Future",
            "description": "Our sensor technology supports the development of smart cities and infrastructure by providing real-time data on traffic flow, energy consumption, and structural health. This data enables efficient urban planning, resource management, and enhanced public safety."
          
        },
        "tab_7": {
            "header": "Other",
            "title": "",
            "description": "By integrating these advanced sensor technologies, our platform drives innovation across these and other industries, enabling the development of cutting-edge solutions and fostering progress in various sectors."
          
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
        "image": "../static/images/platforms/AIDE/index_AIDE/section3.jpg",
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
