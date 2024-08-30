from http import HTTPStatus

import pytest

pytestmark = pytest.mark.asyncio


async def test_add_property(client):
    response = await client.post(
        '/property/',
        json={
            'description': 'test description',
            'number_bedrooms': 'T0',
            'price': 456,
            'area': 456,
            'location': 'test location',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'description': 'test description',
        'number_bedrooms': 'T0',
        'price': 456,
        'area': 456,
        'location': 'test location',
    }


async def test_list_properties_empty(client):
    response = await client.get('/property/')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['properties'] == []


async def test_list_properties_with_properties(client, property):
    response = await client.get('/property/')

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()['properties']) == 1


async def test_list_property_by_id(client, property):
    response = await client.get(f'/property/{property.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': property.id,
        'description': property.description,
        'number_bedrooms': property.number_bedrooms,
        'price': property.price,
        'area': property.area,
        'location': property.location,
    }


async def test_update_property(client, property):
    new_description = 'new decription'

    assert property.description != new_description

    response = await client.patch(
        f'/property/{property.id}',
        json={
            'description': new_description,
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': property.id,
        'description': new_description,
        'number_bedrooms': property.number_bedrooms,
        'price': property.price,
        'area': property.area,
        'location': property.location,
    }


async def test_update_property_not_found(client, property):
    response = await client.patch(
        '/property/777',
        json={
            'description': 'description',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Property ID was not found.'}


async def test_delete_property(client, property):
    response = await client.delete(f'/property/{property.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Property deleted.'}


async def test_delete_property_not_found(client, property):
    response = await client.delete('/property/777')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Property ID was not found.'}
