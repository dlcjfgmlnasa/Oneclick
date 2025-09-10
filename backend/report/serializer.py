# -*- coding:utf-8 -*-
from report.models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            'pk',
            'tib',
            'tst',
            'twt',
            'waso',
            'sleep_latency',
            'rem_latency',
            'sleep_eff',
            'sleep_n1_min',
            'sleep_n2_min',
            'sleep_n3_min',
            'sleep_nrem_min',
            'sleep_rem_min',
            'sleep_n1_tst',
            'sleep_n2_tst',
            'sleep_n3_tst',
            'sleep_nrem_tst',
            'sleep_rem_tst',
        )

