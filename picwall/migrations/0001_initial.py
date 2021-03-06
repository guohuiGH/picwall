# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Picture'
        db.create_table(u'picwall_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pid', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pic_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pic_desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pic_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pic_upload_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('pic_author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'picwall', ['Picture'])

        # Adding model 'PictureComment'
        db.create_table(u'picwall_picturecomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='commenter', to=orm['auth.User'])),
            ('pic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.Picture'])),
            ('published_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'picwall', ['PictureComment'])

        # Adding model 'PhotoWall'
        db.create_table(u'picwall_photowall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='creator+', to=orm['auth.User'])),
            ('create_data', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 6, 6, 0, 0))),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'picwall', ['PhotoWall'])

        # Adding M2M table for field access_users on 'PhotoWall'
        m2m_table_name = db.shorten_name(u'picwall_photowall_access_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photowall', models.ForeignKey(orm[u'picwall.photowall'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photowall_id', 'user_id'])

        # Adding model 'PhotoInformation'
        db.create_table(u'picwall_photoinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.Picture'])),
            ('photo_wall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['picwall.PhotoWall'])),
            ('left', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('top', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('width', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'picwall', ['PhotoInformation'])


    def backwards(self, orm):
        # Deleting model 'Picture'
        db.delete_table(u'picwall_picture')

        # Deleting model 'PictureComment'
        db.delete_table(u'picwall_picturecomment')

        # Deleting model 'PhotoWall'
        db.delete_table(u'picwall_photowall')

        # Removing M2M table for field access_users on 'PhotoWall'
        db.delete_table(db.shorten_name(u'picwall_photowall_access_users'))

        # Deleting model 'PhotoInformation'
        db.delete_table(u'picwall_photoinformation')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'picwall.photoinformation': {
            'Meta': {'object_name': 'PhotoInformation'},
            'height': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'photo_wall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.PhotoWall']"}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.Picture']"}),
            'top': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'width': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'picwall.photowall': {
            'Meta': {'object_name': 'PhotoWall'},
            'access_users': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'access_user_+'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'create_data': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 6, 6, 0, 0)'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'creator+'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'picwall.picture': {
            'Meta': {'object_name': 'Picture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic_author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'pic_desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pic_upload_time': ('django.db.models.fields.DateTimeField', [], {}),
            'pic_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pid': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'picwall.picturecomment': {
            'Meta': {'ordering': "('published_date',)", 'object_name': 'PictureComment'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'commenter'", 'to': u"orm['auth.User']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['picwall.Picture']"}),
            'published_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['picwall']