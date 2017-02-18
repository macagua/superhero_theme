{
    # Theme information
    'name': "Bootswatch Superhero Theme",
    'summary': 'Support for Bootswatch Superhero theme',
    'description': 'This theme module is exclusively for master theme to keep the support of Bootswatch Superhero Theme into Odoo 9.',
    'category': 'Theme',
    'version': '1.0',
    'depends': ['website'],
    'images': ['static/description/bootswatch_superhero.png'],
    'application': False,

    # templates
    'data': [
        'views/pages.xml',
        # 'views/options.xml',
        # 'views/snippets.xml',
    ],

    # demo pages
    # 'demo': [
    #     'demo/pages.xml',
    # ],

    # Your information
    'author': "Leonardo J. Caballero G.",
    'website': "https://lcaballero.wordpress.com/",
}

