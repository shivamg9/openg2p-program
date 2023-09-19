# Part of OpenG2P. See LICENSE file for full copyright and licensing details.
{
    "name": "OpenG2P Programs",
    "category": "G2P/G2P",
    "version": "15.0.1.2.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "base",
        "mail",
        "g2p_registry_base",
        "g2p_registry_individual",
        "g2p_registry_group",
        "g2p_registry_membership",
        "g2p_bank",
        "l10n_generic_coa",
        "event_sms",
        "calendar",
    ],
    "data": [
        "security/program_security.xml",
        "security/ir.model.access.csv",
        "security/registrant_rule.xml",
        "data/sequences.xml",
        "report/voucher_card.xml",
        "report/report_format.xml",
        "views/main_view.xml",
        "views/programs_view.xml",
        "views/program_membership_view.xml",
        "views/cycle_view.xml",
        "views/cycle_membership_view.xml",
        "views/entitlement_view.xml",
        "views/payment_view.xml",
        "views/payment_batch_view.xml",
        "views/payment_batch_tag_view.xml",
        "views/registrant_view.xml",
        "views/managers/eligibility_manager_view.xml",
        "views/managers/deduplication_manager_view.xml",
        "views/managers/notification_manager_view.xml",
        "views/managers/program_manager_view.xml",
        "views/managers/cycle_manager_view.xml",
        "views/managers/entitlement_manager_view.xml",
        "views/managers/payment_manager_view.xml",
        "views/accounting/fund_management_view.xml",
        "views/accounting/account_journal_view.xml",
        "views/accounting/fund_report_view.xml",
        "views/accounting/account_journal_config_view.xml",
        "views/duplicate_view.xml",
        "wizard/assign_to_program_wizard.xml",
        "wizard/multi_entitlement_approval_wizard.xml",
        "wizard/create_program_wizard.xml",
        "wizard/assign_payments_batch_wizard.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "/g2p_programs/static/src/js/create_program.js",
        ],
        "web.assets_qweb": [
            "/g2p_programs/static/src/xml/create_program_template.xml",
        ],
    },
    "demo": [],
    "images": [],
    "external_dependencies": {
        "python": [
            "python-dateutil",
        ]
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
