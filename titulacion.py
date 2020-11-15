class Titulacion(models.Model):
     _name = 'upobye.Titulacion'
     _description = 'upobye Titulacion'
     nombre = fields.Char(string="Nombre", required=True, help="Nombre")
     description = fields.Text()
     certificacion = fields.Char(string="certificacion", required=True, help="Certificacion")
