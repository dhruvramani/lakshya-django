# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LakskhyaTestimonial'
        db.delete_table('utils_lakskhyatestimonial')

        # Adding model 'LakshyaTestimonial'
        db.create_table('utils_lakshyatestimonial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testimonial_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('video_link', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_of_entry', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True)),
            ('sorting', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('utils', ['LakshyaTestimonial'])


    def backwards(self, orm):
        # Adding model 'LakskhyaTestimonial'
        db.create_table('utils_lakskhyatestimonial', (
            ('date_of_entry', self.gf('django.db.models.fields.DateField')(auto_now=True, null=True, blank=True)),
            ('sorting', self.gf('django.db.models.fields.IntegerField')()),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testimonial_text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('utils', ['LakskhyaTestimonial'])

        # Deleting model 'LakshyaTestimonial'
        db.delete_table('utils_lakshyatestimonial')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'people.person': {
            'Meta': {'object_name': 'Person'},
            'billing_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'billing_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'billing_country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'billing_landmark': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'billing_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'billing_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'course': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_nitw_alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pan_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'profile_pic': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'year_of_passing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'utils.lakshyatestimonial': {
            'Meta': {'object_name': 'LakshyaTestimonial'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_of_entry': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']"}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sorting': ('django.db.models.fields.IntegerField', [], {}),
            'testimonial_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video_link': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'utils.lakshyaupdate': {
            'Meta': {'object_name': 'LakshyaUpdate'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_of_entry': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sorting': ('django.db.models.fields.IntegerField', [], {}),
            'update_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['utils']