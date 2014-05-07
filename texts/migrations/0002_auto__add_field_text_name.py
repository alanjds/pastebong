# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Text.name'
        db.add_column(u'texts_text', 'name',
                      self.gf('django.db.models.fields.CharField')(default='DEADBEEF', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Text.name'
        db.delete_column(u'texts_text', 'name')


    models = {
        u'texts.text': {
            'Meta': {'object_name': 'Text'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'filetype': ('django.db.models.fields.CharField', [], {'default': "'python'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['texts']