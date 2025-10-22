# © 2016-2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Developer Profile',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'license': 'AGPL-3',
    'summary': 'Developer Profile',
    'description': """Add modules and set parameters that are usefull to develop and test on Odoo.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': [
        # BASE
        'base_profile_akretion',
        'web_dark_mode',
        # Don't depend on partner_bank_acc_type_constraint
        # because it blocks the demo data of account_statement_import_file
        # and probably other modules
        #'partner_bank_acc_type_constraint',
        'auth_admin_passkey',
        #'web_translate_dialog',
        'phone_validation',
        #'base_phone',
        # PRODUCT
        'product_usability',
        # SALE
        'sale_crm',
        'sale_management',
        'crm_usability',
        'sale_usability',
        'sale_stock_usability',
        'sale_commercial_partner',
        # PURCHASE
        'purchase_usability',
        'purchase_commercial_partner',
        'purchase_stock_usability',
        # PROCUREMENT
        # STOCK
        'stock_usability',
 #       'stock_account_usability',
        'delivery_usability',
        # MRP
        'mrp_usability',
        # POS
        'pos_usability',
        'pos_payment_change',
        # ACCOUNT
        'l10n_fr_account_profile_akretion',
 #       'account_fiscal_year',
        'account_banking_sepa_credit_transfer',
        'account_payment_sale',
        'account_check_deposit',
        'account_cash_deposit',
        'account_invoice_transmit_method',
        'l10n_fr_intrastat_product',
        'account_statement_completion_label_simple_sale',
        'account_cutoff_start_end_dates',
        ],
    'data': [
        'profile.xml',
    ],
#    'demo': ['demo.xml'],
    'installable': True,
}
