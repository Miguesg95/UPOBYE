class Idioma(models.Model):
     _name = 'upobye.Idioma'
     _description = 'upobye Idioma'
     nombre = fields.Char(string="Nombre", required=True, help="Nombre")
     certificacion = fields.Char(string="certificacion", required=True, help="Certificacion")

