# © 2016-2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Developer Profile',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'license': 'AGPL-3',
    'summary': 'Developer Profile',
    'description': """Add modules and set parameters that are usefull to develop and test on Odoo.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
        # BASE
        'disable_odoo_online',
        'base_usability',
        #'mail_usability',
        'base_import',
        'base_technical_features',
        'base_company_extension',
        'partner_disable_gravatar',
        'auth_admin_passkey',
        #'web_export_view',
        #'web_no_bubble',  # plus besoin
        #'eradicate_quick_create',  # plus besoin, nouveau popup
        'web_dialog_size',
        #'web_translate_dialog',
        'phone_validation',
        #'base_phone',
        # PRODUCT
        'product_usability',
        # SALE
        'sale_crm',
        'sale_management',
        #'crm_usability',
        'sale_usability',
        'sale_stock_usability',
        'sale_commercial_partner',
        # PURCHASE
        'purchase_usability',
        'purchase_commercial_partner',
        'purchase_stock_usability',
        # PROCUREMENT
        #'procurement_suggest',
        # STOCK
        'sale_stock',
        'stock_usability',
        'stock_account_usability',
        #'delivery_usability',
        # MRP
        'mrp_usability',
        # POS
        'point_of_sale',
        'pos_usability',
        # ACCOUNT
        'account_usability',
        'account_menu',
        'l10n_fr_fec_oca',
        'account_fiscal_year',
        'account_financial_report',
        'account_banking_sepa_credit_transfer',
        'account_check_deposit',
        'account_move_csv_import',
        'account_statement_import_ofx',
        'account_statement_import_fr_cfonb',
        'account_usability',
        'account_reconciliation_widget',
        #'account_bank_statement_import_usability',
        'account_fiscal_position_vat_check',
        'account_lock_date_update',
        'l10n_fr_das2',
        'l10n_fr_mis_reports',
        'account_balance_ebp_csv_export',
        'account_invoice_transmit_method',
        'account_invoice_overdue_reminder',
        'l10n_fr_intrastat_product',
        'l10n_fr_intrastat_service',
        'l10n_fr_siret',
        'account_statement_completion_label_simple',
        #'account_invoice_fiscal_position_update',
        #'account_bank_statement_no_reconcile_guess',
        #'account_bank_reconciliation_summary_xlsx',
        ],
    'data': [
        'profile.xml',
    ],
#    'demo': ['demo.xml'],
    'installable': True,
}
