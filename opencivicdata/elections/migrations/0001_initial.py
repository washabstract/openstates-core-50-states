# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 15:20
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import opencivicdata.core.models.base
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BallotMeasureContest',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(help_text='Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.', ocd_type='contest', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='Name of the contest, not necessarily as it appears on the ballot.', max_length=300)),
                ('description', models.TextField(help_text='Text describing the purpose and/or potential outcomes of the ballot measure, not necessarily as it appears on the ballot.')),
                ('requirement', models.CharField(blank=True, default='50% plus one vote', help_text='The threshold of votes the ballot measure needs in order to pass.', max_length=300)),
                ('classification', models.CharField(blank=True, help_text='Describes the origin and/or potential outcome of the ballot measure, e.g., "initiative statute", "legislative constitutional amendment".', max_length=300)),
                ('division', models.ForeignKey(help_text="Reference to the Division that defines the political geography of the contest, e.g., a specific Congressional or State Senate district. Should be a subdivision of the Division referenced by the contest's Election.", on_delete=django.db.models.deletion.CASCADE, related_name='ballotmeasurecontests', related_query_name='ballotmeasurecontests', to='core.Division')),
            ],
            options={
                'db_table': 'opencivicdata_ballotmeasurecontest',
            },
        ),
        migrations.CreateModel(
            name='BallotMeasureContestIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('contest', models.ForeignKey(help_text='Reference to the BallotMeasureContest linked to the upstream identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='elections.BallotMeasureContest')),
            ],
            options={
                'db_table': 'opencivicdata_ballotmeasurecontestidentifier',
            },
        ),
        migrations.CreateModel(
            name='BallotMeasureContestOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Text of the option, not necessarily as it appears on the ballot.', max_length=300)),
                ('contest', models.ForeignKey(help_text='Reference to the BallotMeasureContest.', on_delete=django.db.models.deletion.CASCADE, related_name='options', to='elections.BallotMeasureContest')),
            ],
            options={
                'db_table': 'opencivicdata_ballotmeasurecontestoption',
            },
        ),
        migrations.CreateModel(
            name='BallotMeasureContestSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('contest', models.ForeignKey(help_text='Reference to the BallotMeasureContest assembled from the source.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='elections.BallotMeasureContest')),
            ],
            options={
                'db_table': 'opencivicdata_ballotmeasurecontestsource',
            },
        ),
        migrations.CreateModel(
            name='Candidacy',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(help_text='Open Civic Data-style id in the format ``ocd-candidacy/{{uuid}}``.', ocd_type='candidacy', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-candidacy/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-candidacy/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('candidate_name', models.CharField(help_text="For preserving the candidate's name as it was of the candidacy.", max_length=300)),
                ('filed_date', models.DateField(help_text='Specifies when the candidate filed for the contest.', null=True)),
                ('is_incumbent', models.NullBooleanField(help_text='Indicates whether the candidate is seeking re-election to a public office he/she currently holds')),
                ('registration_status', models.CharField(choices=[('filed', 'Filed'), ('qualified', 'Qualified'), ('withdrawn', 'Withdrawn'), ('write-in', 'Write-in')], help_text='Registration status of the candidate.', max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'candidacies',
                'db_table': 'opencivicdata_candidacy',
                'ordering': ('contest', 'post', 'person'),
            },
        ),
        migrations.CreateModel(
            name='CandidacySource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('candidacy', models.ForeignKey(help_text='Reference to the assembed Candidacy.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='elections.Candidacy')),
            ],
            options={
                'db_table': 'opencivicdata_candidacysource',
            },
        ),
        migrations.CreateModel(
            name='CandidateContest',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(help_text='Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.', ocd_type='contest', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='Name of the contest, not necessarily as it appears on the ballot.', max_length=300)),
                ('previous_term_unexpired', models.BooleanField(default=False, help_text='Indicates the previous public office holder vacated the post before serving a full term.')),
                ('number_elected', models.IntegerField(default=1, help_text="Number of candidates that are elected in the contest, i.e. 'N' of N-of-M.")),
                ('division', models.ForeignKey(help_text="Reference to the Division that defines the political geography of the contest, e.g., a specific Congressional or State Senate district. Should be a subdivision of the Division referenced by the contest's Election.", on_delete=django.db.models.deletion.CASCADE, related_name='candidatecontests', related_query_name='candidatecontests', to='core.Division')),
            ],
            options={
                'db_table': 'opencivicdata_candidatecontest',
            },
        ),
        migrations.CreateModel(
            name='CandidateContestIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('contest', models.ForeignKey(help_text='Reference to the CandidateContest linked to the upstream identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='elections.CandidateContest')),
            ],
            options={
                'db_table': 'opencivicdata_candidatecontestidentifier',
            },
        ),
        migrations.CreateModel(
            name='CandidateContestPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(default=0, help_text='Useful for sorting for contests where two or more public offices are at stake, e.g., in a U.S. presidential contest, the President post would have a lower sort order than the Vice President post.')),
                ('contest', models.ForeignKey(help_text='Reference to the CandidateContest in which the Post is at stake.', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='elections.CandidateContest')),
                ('post', models.ForeignKey(help_text='Reference to the Post at stake in the CandidateContest.', on_delete=django.db.models.deletion.CASCADE, related_name='contests', to='core.Post')),
            ],
            options={
                'db_table': 'opencivicdata_candidatecontestpost',
                'ordering': ('contest', 'sort_order'),
            },
        ),
        migrations.CreateModel(
            name='CandidateContestSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('contest', models.ForeignKey(help_text='Reference to the CandidateContest assembled from the source.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='elections.CandidateContest')),
            ],
            options={
                'db_table': 'opencivicdata_candidatecontestsource',
            },
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(help_text='Open Civic Data-style id in the format ``ocd-election/{{uuid}}``.', ocd_type='election', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-election/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-election/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='Name of the Election.', max_length=300)),
                ('date', models.DateField(help_text="Final or only date when eligible voters may cast their ballots in the Election. Typically this is also the same date when results of the election's contests are first publicly reported.")),
                ('administrative_organization', models.ForeignKey(help_text='Reference to the Organization that administers the election.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='elections', to='core.Organization')),
                ('division', models.ForeignKey(help_text='Reference to the Division that defines the broadest political geography of any contest to be decided by the election.', on_delete=django.db.models.deletion.CASCADE, related_name='elections', to='core.Division')),
            ],
            options={
                'db_table': 'opencivicdata_election',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ElectionIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('election', models.ForeignKey(help_text='Reference to the Election identified by the identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='elections.Election')),
            ],
            options={
                'db_table': 'opencivicdata_electionidentifier',
            },
        ),
        migrations.CreateModel(
            name='ElectionSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='elections.Election')),
            ],
            options={
                'db_table': 'opencivicdata_electionsource',
            },
        ),
        migrations.CreateModel(
            name='PartyContest',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(help_text='Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.', ocd_type='contest', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='Name of the contest, not necessarily as it appears on the ballot.', max_length=300)),
                ('division', models.ForeignKey(help_text="Reference to the Division that defines the political geography of the contest, e.g., a specific Congressional or State Senate district. Should be a subdivision of the Division referenced by the contest's Election.", on_delete=django.db.models.deletion.CASCADE, related_name='partycontests', related_query_name='partycontests', to='core.Division')),
                ('election', models.ForeignKey(help_text='Reference to the Election in which the contest is decided.', on_delete=django.db.models.deletion.CASCADE, related_name='partycontests', related_query_name='partycontests', to='elections.Election')),
                ('runoff_for_contest', models.OneToOneField(help_text='If this contest is a runoff to determine the outcome of a previously undecided contest, reference to that PartyContest.', null=True, on_delete=django.db.models.deletion.CASCADE, to='elections.PartyContest')),
            ],
            options={
                'db_table': 'opencivicdata_partycontest',
            },
        ),
        migrations.CreateModel(
            name='PartyContestIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('contest', models.ForeignKey(help_text='Reference to the PartyContest linked to the upstream identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='elections.PartyContest')),
            ],
            options={
                'db_table': 'opencivicdata_partyidentifier',
            },
        ),
        migrations.CreateModel(
            name='PartyContestOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_incumbent', models.NullBooleanField(help_text='Indicates whether the party currently holds majority power.')),
                ('contest', models.ForeignKey(help_text='Reference to the PartyContest in which the Party is an option.', on_delete=django.db.models.deletion.CASCADE, related_name='parties', to='elections.PartyContest')),
                ('party', models.ForeignKey(help_text='Reference to the Party option in the PartyContest.', on_delete=django.db.models.deletion.CASCADE, related_name='party_contests', to='core.Organization')),
            ],
            options={
                'db_table': 'opencivicdata_partycontestoption',
                'ordering': ('contest', 'party'),
            },
        ),
        migrations.CreateModel(
            name='PartyContestSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('contest', models.ForeignKey(help_text='Reference to the PartyContest assembled from the source.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='elections.PartyContest')),
            ],
            options={
                'db_table': 'opencivicdata_partysource',
            },
        ),
        migrations.CreateModel(
            name='RetentionContest',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('locked_fields', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, default=list, size=None)),
                ('id', opencivicdata.core.models.base.OCDIDField(help_text='Open Civic Data-style id in the format ``ocd-contest/{{uuid}}``.', ocd_type='contest', serialize=False, validators=[django.core.validators.RegexValidator(flags=32, message='ID must match ^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', regex='^ocd-contest/[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$')])),
                ('name', models.CharField(help_text='Name of the contest, not necessarily as it appears on the ballot.', max_length=300)),
                ('description', models.TextField(help_text='Text describing the purpose and/or potential outcomes of the contest, not necessarily as it appears on the ballot.')),
                ('requirement', models.CharField(blank=True, default='50% plus one vote', help_text='The threshold of votes need in order to retain the officeholder.', max_length=300)),
                ('division', models.ForeignKey(help_text="Reference to the Division that defines the political geography of the contest, e.g., a specific Congressional or State Senate district. Should be a subdivision of the Division referenced by the contest's Election.", on_delete=django.db.models.deletion.CASCADE, related_name='retentioncontests', related_query_name='retentioncontests', to='core.Division')),
                ('election', models.ForeignKey(help_text='Reference to the Election in which the contest is decided.', on_delete=django.db.models.deletion.CASCADE, related_name='retentioncontests', related_query_name='retentioncontests', to='elections.Election')),
                ('membership', models.ForeignKey(help_text='Reference to the Membership that represents the tenure of a person in a specific public office.', on_delete=django.db.models.deletion.CASCADE, to='core.Membership')),
                ('runoff_for_contest', models.OneToOneField(help_text='If this contest is a runoff to determine the outcome of a previously undecided contest, reference to that RetentionContest.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runoff_contest', to='elections.RetentionContest')),
            ],
            options={
                'db_table': 'opencivicdata_retentioncontest',
            },
        ),
        migrations.CreateModel(
            name='RetentionContestIdentifier',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=300)),
                ('scheme', models.CharField(max_length=300)),
                ('contest', models.ForeignKey(help_text='Reference to the RetentionContest linked to the upstream identifier.', on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='elections.RetentionContest')),
            ],
            options={
                'db_table': 'opencivicdata_retentionidentifier',
            },
        ),
        migrations.CreateModel(
            name='RetentionContestOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='Text of the option, not necessarily as it appears on the ballot.', max_length=300)),
                ('contest', models.ForeignKey(help_text='Reference to the RetentionContest.', on_delete=django.db.models.deletion.CASCADE, related_name='options', to='elections.RetentionContest')),
            ],
            options={
                'db_table': 'opencivicdata_retentioncontestoption',
            },
        ),
        migrations.CreateModel(
            name='RetentionContestSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=300)),
                ('url', models.URLField(max_length=2000)),
                ('contest', models.ForeignKey(help_text='Reference to the RetentionContest assembled from the source.', on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='elections.RetentionContest')),
            ],
            options={
                'db_table': 'opencivicdata_retentionsource',
            },
        ),
        migrations.AddField(
            model_name='candidatecontest',
            name='election',
            field=models.ForeignKey(help_text='Reference to the Election in which the contest is decided.', on_delete=django.db.models.deletion.CASCADE, related_name='candidatecontests', related_query_name='candidatecontests', to='elections.Election'),
        ),
        migrations.AddField(
            model_name='candidatecontest',
            name='party',
            field=models.ForeignKey(help_text='If the contest is among candidates of the same political party, e.g., a partisan primary election, reference to the Party.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidate_contests', to='core.Organization'),
        ),
        migrations.AddField(
            model_name='candidatecontest',
            name='runoff_for_contest',
            field=models.OneToOneField(help_text='If this contest is a runoff to determine the outcome of a previously undecided contest, reference to that CandidateContest.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runoff_contest', to='elections.CandidateContest'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='contest',
            field=models.ForeignKey(help_text='Reference to an OCD CandidateContest representing the contest in which the candidate is competing.', on_delete=django.db.models.deletion.CASCADE, related_name='candidacies', to='elections.CandidateContest'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='party',
            field=models.ForeignKey(help_text='Reference to and Party with which the candidate is affiliated.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidacies', to='core.Organization'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='person',
            field=models.ForeignKey(help_text='Reference to the Person who is the candidate.', on_delete=django.db.models.deletion.CASCADE, related_name='candidacies', to='core.Person'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='post',
            field=models.ForeignKey(help_text='Reference to Post represents the public office for which the candidate is competing.', on_delete=django.db.models.deletion.CASCADE, related_name='candidacies', to='core.Post'),
        ),
        migrations.AddField(
            model_name='candidacy',
            name='top_ticket_candidacy',
            field=models.ForeignKey(help_text='If the candidate is running as part of ticket, e.g., a Vice Presidential candidate running with a Presidential candidate, reference to candidacy at the top of the ticket.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='elections.Candidacy'),
        ),
        migrations.AddField(
            model_name='ballotmeasurecontest',
            name='election',
            field=models.ForeignKey(help_text='Reference to the Election in which the contest is decided.', on_delete=django.db.models.deletion.CASCADE, related_name='ballotmeasurecontests', related_query_name='ballotmeasurecontests', to='elections.Election'),
        ),
        migrations.AddField(
            model_name='ballotmeasurecontest',
            name='runoff_for_contest',
            field=models.OneToOneField(help_text='If this contest is a runoff to determine the outcome of a previously undecided contest, reference to that BallotMeasureContest.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runoff_contest', to='elections.BallotMeasureContest'),
        ),
    ]