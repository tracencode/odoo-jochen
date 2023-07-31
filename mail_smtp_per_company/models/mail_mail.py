# -*- coding: utf-8 -*-
from odoo import models, fields


class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'

    company_id = fields.Many2one('res.company', string='Company', required=True, index=True, default=lambda self: self.env.user.company_id,)

class MailMail(models.Model):
    _inherit = 'mail.mail'

    def send(self, auto_commit=False, raise_exception=False):
        company_id = self.env.company or self.env.user.company_id
        for email in self.env['mail.mail'].browse(self.ids):
            if email.attachment_ids:
                company_id = email.attachment_ids[0].company_id
            server_id = self.env['ir.mail_server'].search([
                ('company_id', '=', company_id.id)])
            server_id = server_id and server_id[0] or False
            if server_id:
                self.write(
                    {'mail_server_id': server_id[0].id})
        return super(MailMail, self).send(auto_commit=auto_commit,
                                          raise_exception=raise_exception)
