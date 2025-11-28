# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import relativedelta
import re

class Alumno(models.Model):
    _name = 'participantes.alumno'
    _description = 'Define los atributos de un alumno'
    _rec_name = 'nombreAlumno'

    nombreAlumno = fields.Char(string='Nombre del Alumno', required=True)
    apellidoAlumno = fields.Char(string='Apellido del Alumno',required=True)
    fechaAlumno = fields.Date(string='Fecha Nacimiento del Alumno',required=True)
    cursoAlumno = fields.Selection([
        ('1ºeso', '1ºESO'),
        ('2ºeso', '2ºESO'),
        ('3ºeso', '3ºESO'),
        ('4ºeso', '4ºESO'),
        ('1ºbach', '1ºBACH'),
        ('2ºbach', '2ºBACH')
    ], string='Curso del Alumno', default='1ºeso',required=True)
    
    excursiones_ids = fields.Many2many(
        comodel_name='excursiones.excursion', 
        relation='excursion_alumno_rel',        
        column1='alumno_id',                    
        column2='excursion_id',                 
        string='Excursiones Inscritas'
    )

    @api.constrains('fechaAlumno')
    def _check_fecha(self):
        hoy = date.today()
        fechaMayor = hoy - relativedelta(years=5)
        for alumno in self:
            if (alumno.fechaAlumno > hoy or alumno.fechaAlumno > fechaMayor):
                raise exceptions.ValidationError(" La Fecha de Nacimiento del Alumno debe ser IGUAL o INFERIOR a Hoy (Minimo de 5 años).")
    

class Autorizacion(models.Model):
    _name = 'participantes.autorizacion'
    _description = 'Define los atributos de la autorizacion'
    _rec_name = 'tutorAlumno'

    tutorAlumno = fields.Char(string='Tutor del alumno (Padre/Madre)', required=True)
    telefono = fields.Char(string='Teléfono del Tutor')
    direccion = fields.Char(string='Dirección del Tutor')
    email = fields.Char(string='Correo electrónico del Tutor')
    diaAutorizar = fields.Date(string='Fecha de la Autorizacion Firmada',default=fields.Date.today)

    alumno_id = fields.Many2one('participantes.alumno', string='Alumno autorizado')

    @api.constrains('diaAutorizar')
    def _check_fecha(self):
        hoy = date.today()
        for autorizacion in self:
            if (autorizacion.diaAutorizar > hoy):
                raise exceptions.ValidationError(" La Fecha de la Autorizacion debe ser igual o inferior a Hoy.")

    @api.constrains('telefono')
    def _check_telefono(self):
        for profe in self:
            if profe.telefono and (not profe.telefono.isdigit() or len(profe.telefono) != 9):
                raise exceptions.ValidationError("El Teléfono debe contener exactamente 9 números.")

    @api.constrains('email')
    def _check_email(self):
        for profe in self:
            if profe.email and '@' not in profe.email:
                raise exceptions.ValidationError("El Correo Electrónico debe contener un '@'.")

