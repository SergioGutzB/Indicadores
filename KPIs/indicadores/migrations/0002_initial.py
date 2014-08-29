# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Indicador'
        db.create_table(u'indicadores_indicador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Descripcion_Concepto', self.gf('django.db.models.fields.TextField')()),
            ('Descripcion_Operacion', self.gf('django.db.models.fields.TextField')()),
            ('Otro', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'indicadores', ['Indicador'])


    def backwards(self, orm):
        # Deleting model 'Indicador'
        db.delete_table(u'indicadores_indicador')


    models = {
        u'indicadores.indicador': {
            'Descripcion_Concepto': ('django.db.models.fields.TextField', [], {}),
            'Descripcion_Operacion': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'Indicador'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Otro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['indicadores']