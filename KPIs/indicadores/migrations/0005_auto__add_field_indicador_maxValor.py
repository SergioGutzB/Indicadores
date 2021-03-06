# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Indicador.maxValor'
        db.add_column(u'indicadores_indicador', 'maxValor',
                      self.gf('django.db.models.fields.TextField')(default=4),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Indicador.maxValor'
        db.delete_column(u'indicadores_indicador', 'maxValor')


    models = {
        u'indicadores.indicador': {
            'Descripcion_Concepto': ('django.db.models.fields.TextField', [], {}),
            'Descripcion_Operacion': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'Indicador'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Otro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxValor': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['indicadores']