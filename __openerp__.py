{
    # Theme information
    'name': "superheroe_theme",
    'description': """ Example of a bootstrap theme moved into Odoo 9!
    """,
    'category': 'Theme',
    'version': '1.0',
    'depends': ['website'],

    # templates
    'data': [
        'views/pages.xml',
        # 'views/options.xml',
        # 'views/snippets.xml',
    ],

    # demo pages
    'demo': [
        'demo/pages.xml',
    ],

    # Your information
    'author': "Leonardo J. Caballero G.",
    'website': "https://lcaballero.wordpress.com/",
}