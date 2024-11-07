{
    "name": "ICA E-Learning",
    "license": "LGPL-3",
    "author": "IdeaCode Academy",
    "depends": ["base", "web", "mail","contacts"],
    "data": [
        "security/elearning_groups.xml",
        "security/ir.model.access.csv",

        "data/ir_sequence.xml",
        "views/res_partner.xml",
        "wizard/ica_order_wizard.xml",
        "views/ica_order.xml",
        "views/client_action.xml",
        "views/ica_lesson.xml",
        "views/ica_course.xml",
        "views/menus.xml",

        "report/ica_course_template.xml",
        "report/ica_course_reports.xml",
    ],
    "assets":{
        "web.assets_backend":[
            "ica_elearning/static/src/client_action/**/*",
        ]
    }
}
