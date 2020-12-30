from odoo import models


class ThemeBiovum(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_biovum_post_copy(self, mod):
        self.disable_view('website_theme_install.customize_modal')
