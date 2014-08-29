# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Indicador.Valor'
        db.delete_column(u'indicadores_indicador', 'Valor')


    def backwards(self, orm):
        # Adding field 'Indicador.Valor'
        db.add_column(u'indicadores_indicador', 'Valor',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


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