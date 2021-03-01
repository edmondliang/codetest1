import os
import vcr

CURRENT_PATH = os.path.dirname(__file__)
HTTP_VCR = vcr.config.VCR(
    cassette_library_dir=os.path.join(CURRENT_PATH, 'data'),
    serializer='yaml',
    path_transformer=vcr.config.VCR.ensure_suffix('.yaml'),
    record_mode='once'
)


@HTTP_VCR.use_cassette
def test_get_users(client):
    r = client.get('/')
    result = r.get_json()
    assert result
    assert len(result) == 35


@HTTP_VCR.use_cassette
def test_registered_user_format(client):
    r = client.get('/')
    result = r.get_json()
    record = next(filter(lambda r: r['id'] == "3", result))
    assert record
    assert record['projectIds'] == ['3']
    assert record['emailAddress'] == 'last3@mail.com'
    assert record['company'] == 'Jacobi, Mills and Hills'


@HTTP_VCR.use_cassette
def test_unregister_user_format(client):
    r = client.get('/')
    result = r.get_json()
    record = next(filter(lambda r: r['id'] == '21', result))
    assert record
    assert record['projectIds'] == ['21']
    assert record['emailAddress'] == 'email1@somewhere.com'
    assert not record.get('company')
