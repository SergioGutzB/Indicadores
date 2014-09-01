# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tipo_indicador'
        db.create_table(u'indicadores_tipo_indicador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Descripcion_Concepto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'indicadores', ['Tipo_indicador'])

        # Adding model 'Indicador'
        db.create_table(u'indicadores_indicador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indicadores.Tipo_indicador'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('valor_estimado', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('valor_real', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'indicadores', ['Indicador'])


    def backwards(self, orm):
        # Deleting model 'Tipo_indicador'
        db.delete_table(u'indicadores_tipo_indicador')

        # Deleting model 'Indicador'
        db.delete_table(u'indicadores_indicador')


    models = {
        u'indicadores.indicador': {
            'Meta': {'object_name': 'Indicador'},
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['indicadores.Tipo_indicador']"}),
            'valor_estimado': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'valor_real': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'})
        },
        u'indicadores.tipo_indicador': {
            'Descripcion_Concepto': ('django.db.models.fields.TextField', [], {}),
            'Meta': {'object_name': 'Tipo_indicador'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['indicadores']