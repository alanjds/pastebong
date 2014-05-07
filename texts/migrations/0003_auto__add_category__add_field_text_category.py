# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'texts_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['texts.Category'], null=True, blank=True)),
        ))
        db.send_create_signal(u'texts', ['Category'])

        # Adding field 'Text.category'
        db.add_column(u'texts_text', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['texts.Category']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'texts_category')

        # Deleting field 'Text.category'
        db.delete_column(u'texts_text', 'category_id')


    models = {
        u'texts.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['texts.Category']", 'null': 'True', 'blank': 'True'})
        },
        u'texts.text': {
            'Meta': {'object_name': 'Text'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['texts.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'filetype': ('django.db.models.fields.CharField', [], {'default': "'python'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['texts']