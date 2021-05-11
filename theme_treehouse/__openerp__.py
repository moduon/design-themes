{
    'name': 'Treehouse Theme',
    'description': 'Treehouse Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Environment',
    'version': '1.0',
    'author': 'Odoo SA',
    'depends': ['theme_common', 'snippet_google_map'],
    'data': [
        # THEME
        'views/assets.xml',
        'views/images_library.xml',
        'views/images_content.xml',
        'views/layout.xml',
        'views/snippets.xml',
        'views/snippets_options.xml',
        'views/customize_modal.xml',
        # SNIPPETS
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_big_picture.xml',
        'views/snippets/s_well_extended.xml',
        'views/snippets/s_quote_extended.xml',
        'views/snippets/s_panel_extended.xml',
        'views/snippets/s_separator_extended.xml',
        'views/snippets/s_share_extended.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/components.xml',
        'demo/blocks_structure.xml',
        'demo/blocks_content.xml',
        'demo/blocks_features.xml',
        'demo/blocks_default.xml',
    ],
    'images': [
        'static/description/treehouse_cover.jpg',
    ],
    'price': 195,
    'currency': 'EUR',
    'live_test_url': 'https://theme-treehouse.odoo.com/page/demo_page_01',
}
