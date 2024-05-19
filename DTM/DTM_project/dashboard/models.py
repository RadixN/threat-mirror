from django.db import models

# Create your models here.

class ThreatData(models.Model):
    classification_taxonomy = models.CharField(max_length=100,default='unknown')
    classification_type = models.CharField(max_length=100,default='unknown')
    #event_description = models.CharField(max_length=100,default='unknown')
    feed_accuracy = models.FloatField(null=True, blank=True, default=None)
    feed_name = models.CharField(max_length=100,default='unknown')
    feed_provider = models.CharField(max_length=100,default='unknown')
    feed_url = models.URLField(null=True, blank=True, default=None)
    protocol_application = models.CharField(max_length=100,default='unknown')
    source_abuse_contact = models.CharField(max_length=100,default='unknown')
    #source_allocated = models.CharField(max_length=100,default='unknown')   
    source_as_name = models.CharField(max_length=100,default='unknown') 
    source_asn = models.CharField(max_length=100,default='unknown')
    source_geolocation_cc = models.CharField(max_length=100,default='unknown')  
    source_ip = models.CharField(max_length=100,default='unknown')
    source_network = models.CharField(max_length=100,default='unknown') 
    source_registry = models.CharField(max_length=100,default='unknown')    
    time_observation = models.DateTimeField(null=True, blank=True, default=None)
    time_source = models.DateTimeField(null=True, blank=True, default=None)
    extra_blocklist = models.CharField(max_length=100,default='unknown')
    source_fqdn = models.CharField(max_length=100,default='unknown')
    source_port = models.CharField(max_length=100,default='unknown')
    source_url = models.CharField(max_length=100,default='unknown')
    source_urlpath = models.CharField(max_length=100,default='unknown')
    status = models.CharField(max_length=100,default='unknown')
    protocol_transport = models.CharField(max_length=100,default='unknown')
    malware_name = models.CharField(max_length=100,default='vulnerabilities')
    source_reverse_dns = models.CharField(max_length=100,default='unknown')


    class Meta:
        verbose_name_plural = 'Threat Data '

    def __str__(self):
        return f'{self.classification_taxonomy}- {self.classification_type}- {self.feed_accuracy}'
        

