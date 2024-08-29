from http import HTTPStatus

import pytest

pytestmark = pytest.mark.asyncio


async def test_list_properties_empty(client):
    response = await client.get('/property/')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['properties'] == []


async def test_add_property(client):
    response = await client.post(
        '/property/',
        json = {
            'description': 'test description',
            'number_bedrooms': 'T0',
            'price': 456,
            'area': 456,
            'location': 'test location'
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'description': 'test description',
        'number_bedrooms': 'T0',
        'price': 456,
        'area': 456,
        'location': 'test location'
    }


async def test_update_property(client):
    ...