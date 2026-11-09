"""Facts, page meta and copy for the Vital Tone Chiropractic site.

All wording is carried over verbatim from https://www.vitaltonechiro.com/.
In copy strings **text** renders as <strong>text</strong>.
"""

SITE_ORIGIN = 'https://vital-tone-chiro-redesign.metzdevan.workers.dev'

NAME = 'Vital Tone Chiropractic'
EMAIL = 'info@vitaltonechiro.com'
PHONE = '(262) 355-8669'
TEL = 'tel:(262)%20355-8669'
STREET = 'W164N11271 Squire Dr.'
SUITE = 'Suite P2-200'
CITY_LINE = 'Germantown, WI 53022'
FACEBOOK = 'https://www.facebook.com/profile.php?id=61593431190131'
INSTAGRAM = 'https://instagram.com/vitaltonechiropractic'
CORE_IDENTITY = 'https://www.coreidentityco.com'
TAGLINE = 'Setting the tone for your life.'
CTA = 'BEGIN HEALING TODAY'

# Day, displayed hours, and (opens, closes) pairs for structured data.
HOURS = [
    ('Monday', ['10:00am - 1:00pm', '3:00pm - 6:00pm'], [('10:00', '13:00'), ('15:00', '18:00')]),
    ('Tuesday', ['3:00pm - 6:00 pm'], [('15:00', '18:00')]),
    ('Wednesday', ['10:00am - 1:00pm'], [('10:00', '13:00')]),
    ('Thursday', ['10:00am-1:00pm', '3:00pm - 6:00pm'], [('10:00', '13:00'), ('15:00', '18:00')]),
]

NAV = [('Services', '/services-1/'), ('About', '/about/'), ('FAQ', '/faq/'), ('Contact', '/contact/')]

# Path: (title, meta description). The privacy policy has no description on the original site.
META = {
    '/': (
        'Vital Tone Chiropractic | Discover Modern Care – Schedule Now',
        'Experience modern, gentle chiropractic care focused on natural healing and whole-person health at Vital Tone Chiropractic. Reclaim your wellness today.',
    ),
    '/services-1/': (
        'Services | Optimize Health Today — Book Your Session — Vital Tone Chiropractic',
        'Discover neurologically focused chiropractic care at Vital Tone Chiropractic. Support your nervous system, reduce stress, and improve overall health for individuals and families.',
    ),
    '/about/': (
        'Vital Tone Chiropractic | Chiropractor in | Enhance Health Today – Schedule Now — Vital Tone Chiropractic',
        'Vital Tone Chiropractic offers neurologically focused chiropractic care for all ages, promoting natural healing and nervous system balance for improved well-being.',
    ),
    '/faq/': (
        'FAQ | Enhance Wellness Today — Schedule Now — Vital Tone Chiropractic',
        'Discover neurologically focused chiropractic care at Vital Tone Chiropractic. Improve nervous system function, reduce stress, and enhance overall wellness for all ages.',
    ),
    '/contact/': (
        'Contact | Schedule Your Care Today — Vital Tone Chiropractic',
        'Visit Vital Tone Chiropractic to begin your healing journey. Contact us today for personalized chiropractic care and support for a healthier life.',
    ),
    '/privacy-policy/': ('Privacy Policy — Vital Tone Chiropractic', None),
}

# Fields of the original Squarespace form: label, input type, required, autocomplete.
# The 'name' field is a group of the NAME_PARTS inputs, as on the original form.
FORM_FIELDS = [
    ('Name', 'name', True, ''),
    ('Email', 'email', True, 'email'),
    ('Phone', 'tel', False, 'tel'),
    ('What are your main health concerns?', 'textarea', True, ''),
]
NAME_PARTS = [('First Name', 'given-name'), ('Last Name', 'family-name')]
FORM_SUBMIT = 'Submit'

HOME = {
    'eyebrow': 'Open now in Germantown, WI',
    'pillars': ['Personalized Care', 'Natural Healing', 'Modern Technology'],
    'approach_heading': 'Our Approach',
    'approach_lead': 'We help individuals and families reclaim their health and restore optimal function by delivering gentle, neurologically focused chiropractic care that supports the body’s natural ability to heal, adapt, and thrive.',
    'approach_items': [
        ('Modern Technology', 'We use advanced technology, including Insight® scans and digital X-rays, to better understand how your nervous system and spine are functioning. This allows us to create personalized care plans based on objective findings and track your progress throughout your care'),
        ('Personalized Care', 'No two people are the same, and your care shouldn\'t be either. We take the time to understand your health history, goals, and concerns so we can create a care plan tailored specifically to you and your family\'s needs.'),
        ('Natural Healing', 'Our goal is to help your body function the way it was designed to. By improving nervous system communication, we support your body\'s natural ability to heal, adapt, and thrive - without relying on medications or masking symptoms.'),
    ],
    'band': ('We help restore the communication between your', 'brain and your body so you can function at your best.'),
    'form_heading': 'Let us help you <em>start</em><br><em>your new beginning.</em>',
    'form_text': ['We’d love to hear from you!', 'Fill out this form and we will reach back out to set up your first visit.'],
}

SERVICES = {
    'heading': 'Explore Our Services',
    'neuro_heading': 'Neurologically Focused Chiropractic Care',
    'neuro_text': [
        'At Vital Tone Chiropractic, our care is centered around the nervous system—the control center of the body. When communication between the brain and body is clear and uninterrupted, the body can adapt to stress, heal more efficiently, and function at its highest potential.',
        'Modern life is busy, overstimulating, and stressful. Over time, this stress can cause the nervous system to become stuck in fight-or-flight mode, leading to tension, imbalance, and decreased adaptability. Our goal is to help restore balance by improving how your nervous system communicates, allowing your body to move out of stress mode and into a state of healing and regulation.',
    ],
    'audiences': [
        ('Individuals & Adults', 'Whether you’re navigating daily stress, long workdays, physical tension, or simply want to feel more connected and resilient, neurologically focused chiropractic care supports your body’s ability to adapt and function optimally.'),
        ('Pregnancy & Postpartum', 'Pregnancy places unique demands on the nervous system. Gentle chiropractic care can support better adaptation to these changes, helping moms feel more balanced, supported, and connected throughout pregnancy and beyond.'),
        ('Infants & Children', 'From birth onward, the nervous system plays a critical role in development. Our gentle approach is well-suited for children, supporting their growing bodies and helping them adapt to physical, emotional, and environmental stressors.'),
        ('Families', 'We believe chiropractic care is most powerful when it supports the whole family. Our care plans are designed to fit seamlessly into busy schedules, making it easy for families to prioritize their health together.'),
    ],
    'different_heading': ('What Makes Our', 'Care Different?'),
    'different_sub': ('Gentle. Precise.', 'Neurologically Focused.'),
    'different_text': [
        'At Vital Tone Chiropractic, we use **Torque Release Technique (TRT)** - a gentle, highly specific chiropractic technique designed to optimize nervous system function.',
        'Rather than relying on twisting, cracking, or popping, TRT uses a small handheld instrument called the **Integrator** to deliver precise, consistent adjustments. This allows us to make specific corrections while keeping the experience comfortable for patients of all ages.',
        'Our approach is ideal for individuals and families seeking a modern, personalized approach to chiropractic care - one that supports the body\'s natural ability to heal.',
    ],
    'process_heading': 'Our Process',
    # Title, paragraphs before the list, list items, paragraphs after the list.
    'process': [
        ('Nervous System Assessment',
         ['Your first visit begins with a comprehensive assessment focused on how your nervous system is functioning. This may include:'],
         ['A detailed health history', 'Neurological scans', 'Chiropractic Postural X-rays'],
         ['These insights allow us to create a care plan that is specific to your nervous system and your goals.']),
        ('Gentle, Specific Adjustments',
         ['Adjustments are quick and gentle, making them easy to fit into your day, before work, on a lunch break, after school drop-off, or on your way to the gym.', 'Each adjustment is designed to:'],
         ['Improve communication between brain and body', 'Reduce nervous system interference (subluxation)', 'Help the body adapt more efficiently to stress'],
         []),
        ('Personalized Care Plans',
         ['.No two nervous systems are the same. That’s why we create **custom care plans** based on:'],
         ['Your nervous system findings', 'Your lifestyle and stress levels', 'Your personal health goals'],
         ['Our goal is to make care accessible and affordable while honoring the value and impact of neurologically focused chiropractic care.']),
        ('Why Nervous System Care Matters',
         ['The nervous system influences every function in the body, from movement and digestion to sleep, mood, and immune response. When communication is clear, the body can do what it was designed to do.', 'By restoring proper neurological tone, our care helps you:'],
         ['Better handle stress', 'Improve overall function', 'Feel calmer, more energized, and more resilient', 'Support long-term health naturally'],
         []),
    ],
    'welcome': 'Vital Tone Chiropractic is preparing to welcome our very first patients. As we begin serving the Germantown community, we\'ll share real experiences from the individuals and families who entrust us with their care.',
    'first_visit_heading': 'What to expect at your first visit:',
    'first_visit_lead': 'Your first visit is designed to help us understand what’s going on, identify areas that may be affecting your nervous system and spinal function, and determine whether chiropractic care is appropriate for you. This visit will take 45-60 minutes.',
    'first_visit_steps': [
        ('1. Consultation', 'We start by listening.', 'We’ll sit down with you to learn about your health history, your current concerns, and what you’re hoping to accomplish through care. Understanding your health background and getting to know your goals helps us get a clearer picture of you as a whole person and what you’d like to achieve through chiropractic care.'),
        ('2. Neurological Evaluation', 'Next, we take a closer look at how your body is functioning.', 'We’ll perform three CLA Insight™ scans to gather information about your nervous system. These include a thermal scan, a surface EMG scan, and a heart rate variability (HRV) scan. These scans measure different aspects of your body’s nervous system activity and help us better understand patterns of stress and adaptation.'),
        ('3. Digital Postural X-Rays', 'When appropriate, we use digital X-rays to take a closer look at your spine.', 'Chiropractic postural X-rays allow us to evaluate the structure and alignment of your spine. They provide a closer look at your spinal health and reveal details that cannot be assessed through an external examination alone.'),
        ('4. Next Steps', 'We put everything together.', 'At your follow-up visit, we will present more information about chiropractic, our technique, and expectations for care. Our team will then sit down with you to review your case, outline our recommendations based on your individual needs and goals, and answer any questions you have. After reviewing what care will look like, you will have the opportunity to receive your first adjustment!'),
    ],
    'first_visit_cta': 'Begin Healing Today',
    'form_heading': 'Let us help you set the tone for your life.',
    'form_text': ['Fill out this form and we will connect with you to schedule your consultation with us.'],
}

ABOUT = {
    'heading': 'Our Story',
    # Name, image name, alt text, paragraphs.
    'doctors': [
        ('Meet Dr. John Roddick', 'dr-john-roddick', 'Dr. John Roddick standing outdoors in a green field', [
            'Dr. John is from Sparta, Wisconsin, where he grew up wrestling and running cross country. He went on to become a collegiate wrestler at St. Cloud State, where he also pursued a Bachelor of Science degree in Nursing. He got a job in the Neurological Intensive Care Unit at St. Luke’s Medical Center in Milwaukee, where he saw first-hand the long-term consequences of nervous system dysfunction.',
            'After two years of caring for patients with severe neurological trauma and limited recovery options, Dr. John decided he wanted to help people before they reached this point. This led him to pursue his Doctor of Chiropractic degree from Palmer College of Chiropractic in Davenport, Iowa, where he trained in neurologically focused chiropractic care and coached CrossFit.',
            'Dr. John is passionate about caring for individuals and families who want to play an active role in their health. His experience as a coach allows him to educate, motivate, and lead patients as they work toward their health goals.',
            'Outside of the office, Dr. John enjoys staying active, challenging himself through training and endurance events, grilling, and spending time outdoors with his dog.',
        ]),
        ('Meet Dr. Marlee Williams', 'dr-marlee-williams', 'Dr. Marlee Williams standing outdoors in a green field', [
            'Dr. Marlee grew up in Sussex, Wisconsin. With a lifelong passion for health and wellness, she always envisioned a career in healthcare. Playing soccer and staying active led her to pursue an undergraduate degree in Health and Human Performance at the University of Wisconsin–Whitewater. During this time, she became a certified personal trainer and built a strong foundation in the structure and function of the human body.',
            'Dr. Marlee discovered chiropractic after experiencing an injury that ended her soccer career. After trying multiple therapies that addressed her symptoms but failed to provide lasting change, she decided to explore a different approach. Following a few chiropractic adjustments, she noticed not only a significant reduction in pain, but also positive changes in her overall well-being. This experience inspired her to pursue her Doctor of Chiropractic degree from Palmer College of Chiropractic in Davenport, Iowa.',
            'Dr. Marlee has a strong passion for supporting families, pregnant women, and children through chiropractic care. She has deepened her expertise in this area by earning her PX Certification, which focuses on pediatric, prenatal, and family-centered care with an emphasis on nervous system function.',
            'In her free time, Dr. Marlee enjoys hiking with her dog, taking Pilates classes, cooking, reading, live music, and spending time with her friends and family.',
        ]),
    ],
    'philosophy_heading': 'Our Philosophy',
    'philosophy_lead': 'Your body is incredibly intelligent.',
    'philosophy_text': [
        'Every function in your body - from movement and breathing to digestion, sleep, focus, and emotional regulation - is coordinated by your nervous system. When your nervous system functions optimally, your body is better able to adapt to stress and perform as it was meant to.',
        'Rather than simply chasing symptoms, our approach focuses on one of the most important foundations of health - how well your brain communicates with the rest of your body. By improving nervous system function and reducing neurological interference, we help create the conditions for your body to heal, adapt, and thrive naturally.',
    ],
    'mission_heading': 'Our Mission',
    'mission_text': [
        'At Vital Tone Chiropractic, we believe that true health begins with a well-functioning nervous system. We know that when the nervous system functions optimally, your body is better able to heal, adapt, and thrive.',
        'Our mission is to help you restore balance within your nervous system, empowering you to achieve lasting health through natural chiropractic care.',
    ],
    'stages_heading': 'Care for Every Stage of Life',
    'stages_lead': 'We are passionate about caring for individuals and families at every stage of life.',
    'stages_text': [
        'Whether you\'re living with chronic pain, managing the demands of daily stress, preparing your body for pregnancy, or simply striving to feel stronger, healthier, and more resilient, neurologically focused chiropractic care provides a powerful foundation for lasting health.',
        'Our care is designed to fit seamlessly into your life. Each visit is efficient, intentional, and personalized - making it easy to prioritize your health, even with a busy schedule.',
    ],
    'gentle_heading': 'A Gentle, Modern Approach to Chiropractic Care',
    'gentle_lead': 'Vital Tone Chiropractic uses **Torque Release Technique (TRT)** - a gentle, neurologically focused approach to chiropractic care designed to support optimal nervous system function.',
    'gentle_text': [
        'Rather than relying on twisting, cracking, or popping, TRT uses a small handheld instrument called the **Integrator** to deliver precise, consistent adjustments. This allows us to make highly specific corrections while keeping the experience comfortable for patients of all ages, from infants to older adults.',
        'By reducing interference within the nervous system, these gentle adjustments help your body communicate more efficiently, allowing it to better heal, adapt, and function the way it was designed to.',
    ],
    'band': 'Our goal is to help restore balance within your nervous system, empowering you to take charge of your health naturally, so you can live with greater clarity, resilience, and vitality.',
    'form_heading': 'Let us help you start your health journey.',
    'form_text': ['Fill out this form and we will connect with you to schedule your consultation with us.'],
}

FAQ = {
    'heading': 'Your Questions, Answered',
    'items': [
        ('What is neurologically focused chiropractic care?', 'Neurologically focused chiropractic care looks at how well your nervous system is communicating with your body. Instead of only focusing on symptoms, we assess and support the nervous system so your body can better adapt to stress, regulate itself, and function the way it was designed to.'),
        ('Do I need to be in pain to benefit from chiropractic care?', 'No. Many people come to Vital Tone Chiropractic not because they’re in pain, but because they want to handle stress better, feel more balanced, improve sleep, or support overall wellness. Our care is about improving nervous system function, not just addressing discomfort.'),
        ('What makes Vital Tone Chiropractic different from other chiropractic offices?', 'We use Torque Release Technique (TRT), a gentle and specific approach that focuses directly on the nervous system. There is no twisting, cracking, or popping. Our care is modern, calm, and designed to support long-term health for individuals and families.'),
        ('Is chiropractic care safe for children and infants?', 'Yes. Our gentle approach is well-suited for all ages, including infants and children. Adjustments are extremely light and designed to support healthy nervous system development and adaptability as children grow.'),
        ('What can I expect at my first visit?', 'Your first visit includes a detailed health history and a nervous system–focused assessment. This may include neurological scans and postural evaluations to help us understand how your nervous system is functioning. From there, we’ll explain our findings and recommend a personalized care plan.'),
        ('How long do appointments take?', 'Visits are intentionally efficient and typically take just a few minutes. This allows care to fit easily into your day—before work, during a lunch break, or after school drop-off—while still being impactful.'),
        ('How often will I need to get adjusted?', 'Care plans are customized based on your nervous system, goals, and stress levels. Some people benefit from more frequent visits initially, followed by maintenance care. We’ll always explain recommendations clearly so you feel informed and empowered.'),
        ('Do you accept health insurance?', 'Vital Tone is a cash-based practice, which allows us to keep care focused on your individual needs rather than on insurance restrictions or visit limits. This also helps keep pricing and recommendations clear and straightforward. We’re happy to provide a superbill upon request that you can submit to your insurance company for possible reimbursement.'),
        ('Will I get adjusted at my first visit?', 'No, we do not typically adjust new patients at their first appointment. This appointment is for us to get to know you, the state of your nervous system, and your daily stressors. This allows us to provide personalized care plans and to get adjusted at your second visit.'),
    ],
    'form_heading': 'Still have questions?',
    'form_text': ['We’re here to help.', 'If you’re curious whether neurologically focused chiropractic care is right for you or your family, we’d love to connect.'],
}

CONTACT = {
    'heading': 'We’d love to meet you!',
    'office_heading': 'Visit Our Office',
    'contact_label': 'Contact:',
    'hours_label': 'Office Hours:',
    'location_label': 'Office Location:',
}

PRIVACY = {
    'heading': 'Vital Tone Chiropractic Privacy Policy',
    'effective': 'Effective Date: 1/1/2025',
    'intro': 'At Vital Tone Chiropractic, we are committed to protecting the privacy and confidentiality of your personal information. This Communication Privacy Policy outlines how we collect, use, disclose, and safeguard your communication-related data. By engaging with our services, you agree to the terms outlined in this policy.',
    'sections': [
        ('1. Information We Collect:', [
            ('Contact Information:', 'We may collect your name, email address, phone number, and other contact details when you communicate with us.'),
            ('Communication Content:', 'We may collect information related to your communication with us, including emails, messages, and other forms of communication.'),
        ]),
        ('2. How We Use Your Information:', [
            ('Communication Processing:', 'We use your contact information to communicate with you and respond to your inquiries, requests, or concerns.'),
            ('Service-related Communications:', 'We may send you service-related announcements, updates, and administrative messages.'),
            ('Improving Services:', 'Your communication data may be used to analyze trends, track user interactions, and improve our services.'),
        ]),
        ('3. Information Sharing and Disclosure:', [
            ('Third-Party Service Providers:', 'We may engage third-party service providers to assist with communication services. These providers are contractually obligated to maintain the confidentiality and security of your information.'),
            ('Legal Requirements:', 'We may disclose your information if required by law, regulation, or legal process.'),
        ]),
        ('4. Security Measures:', [
            ('Data Security:', 'We implement reasonable security measures to protect against unauthorized access, disclosure, alteration, or destruction of your information.'),
        ]),
        ('5. Your Choices:', [
            ('Opting Out:', 'You may choose not to receive non-essential communications from us by following the opt-out instructions included in the communication.'),
        ]),
        ('6. Information Protection:', [
            ('No Sale or Distribution:', 'Your information will not be sold or distributed to third parties for marketing purposes.'),
        ]),
    ],
    'contact_heading': '7. Contact Information:',
    'phone_display': '262-355-8669',
    'sms_heading': 'SMS Messaging Terms & Conditions:',
    'sms_intro': ['At Vital Tone Chiropractic, you can opt-in to receive text message notifications.', 'About these notifications:'],
    'sms_items': [
        'Notifications may include appointment reminders, updates, and other information related to the services provided by Vital Tone Chiropractic.',
        'Messaging frequency varies.',
        'Standard messaging rates and data charges may apply.',
        'I can opt-out of receiving these SMS messages at any time by replying \'STOP\' or by contacting Vital Tone Chiropractic directly.',
        'I can text \'HELP or OPTIONS\' for help information.',
    ],
    'consent_heading': '9. Consent:',
    'consent': ('By engaging with our services and communicating with us, you consent to the collection, use, and disclosure of your information as described in this Communication Privacy Policy.'),
}
