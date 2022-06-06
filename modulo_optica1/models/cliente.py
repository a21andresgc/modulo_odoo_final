from odoo import api, fields, models

class ClienteOptica(models.Model):
    _name = "optica.cliente"
    _description = "Detalles del cliente"

    nombre = fields.Char(string='Nombre', required = True)
    edad = fields.Char(string='Edad', required = True)
    patologia = fields.Selection([
        ('miopía', 'Miopía'),
        ('hipermetropía', 'Hipermetropía'),
        ('astigmatismo', 'astigmatismo'),
        ('prescibia', 'Prescibia'),
    ], required = True, default = 'miopía')
    dioptrías = fields.Float(String = 'Dioptrías', required = True)