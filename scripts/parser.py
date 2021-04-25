import json
from pymongo import MongoClient
import requests



class Agent:
    def __init__(self, agent_dict):
        self.uri = agent_dict['_uri']
        self.rdf_type = agent_dict['rdf_type']
        self.rdfs_comment = create_array_class(LangString, agent_dict['rdfs_comment'])
        self.schema_address = create_array_class(schema_PostalAddress, agent_dict['schema_address'])
        self.site_homepage = agent_dict['foaf_homepage']
        self.genre = agent_dict['foaf_title']
        self.schema_gender = agent_dict['schema_gender']
        self.schema_fax_number = agent_dict['schema_faxNumber']
        self.schema_telephone = agent_dict['schema_telephone']
        self.schema_email = agent_dict['schema_email']
        self.schema_givenName = agent_dict['schema_givenName']
        self.schema_familyName = agent_dict['schema_familyName']
        self.agreementLicense = agent_dict['agreementLicense']
        self.registeredNumber = agent_dict['registeredNumber']
        self.siret = agent_dict['siret']
        self.apeNaf = agent_dict['apeNaf']
        self.rcs = agent_dict['rcs']
        self.schema_legalName = agent_dict['schema_legalName']
        self.schema_logo = agent_dict['schema_logo']

class Amenity:
    def __init__(self, amenity_dict):
        self.uri = amenity_dict['_uri']
        self.rdf_type = amenity_dict['rdf_type']
        self.rdfs_label = LangString(amenity_dict['rdfs_label'])
        self.available_lang = amenity_dict['availableLanguage']

class ArchitecturalStyle:
    def __init__(self, archi_dict):
        self.uri = archi_dict['_uri']
        self.rdf_type = archi_dict['rdf_type']
        self.rdfs_label = create_array_class(LangString, archi_dict['rdfs_label'])

class City:
    def __init__(self, city_dict):
        self.uri = city_dict['_uri']
        self.rdf_type = city_dict['rdf_type']
        self.department = Departement(city_dict['isPartOfDepartment'])
        self.insee = city_dict['insee']
        self.rdfs_label = LangString(city_dict['rdfs_label'])

class CuisineCategory:
    def __init__(self, cuisine_cat_dict):
        self.uri = cuisine_cat_dict['_uri']
        self.rdf_type = cuisine_cat_dict['rdf_type']
        self.rdfs_label = LangString(cuisine_cat_dict['rdfs_label'])

class Departement:
    def __init__(self, department_dict):
        self.uri = department_dict['_uri']
        self.rdf_type = department_dict['rdf_type']
        self.region = department_dict['isPartOfRegion'] # TODO add Region Class here 
        self.insee = department_dict['insee']
        self.rdfs_label = LangString(department_dict['rdfs_label'])

class Description:
    def __init__(self, description_dict):
        self.uri = description_dict['_uri']
        self.rdf_type = description_dict['rdf_type']
        self.dc_description = create_array_class(LangString, description_dict['dc_description'])
        self.audience = description_dict['isDedicatedTo'] #TODO change to Audience class
        self.short_desc = create_array_class(LangString, description_dict['shortDescription'])

class Feature:
    def __init__(self, feature_dict):
        self.uri = feature_dict['_uri']
        self.rdf_type = feature_dict['rdf_type']
        self.features = None #fill later TODO
        self.charged = feature_dict['charged']
        self.schema_minValue = feature_dict['schema_minValue']
        self.schema_value = feature_dict['schema_value']
        self.schema_maxValue = feature_dict['schema_maxValue']
        self.floor_size = feature_dict['hasFloorSize']
        self.layout = feature_dict['hasLayout']
        self.occupancy = feature_dict['occupancy']
        self.air_conditionning = feature_dict['airConditioning']
        self.seat_count = feature_dict['seatCount']
        self.internet_access = feature_dict['internetAccess']
        self.no_smoking = feature_dict['noSmoking']
        self.pets_allowed = feature_dict['petsAllowed']

class FoodProduct:
    def __init__(self, food_products_dict):
        self.uri = food_products_dict['_uri']
        self.rdf_type = food_products_dict['rdf_type']
        self.rdfs_label = LangString(food_products_dict['rdfs_label'])

class GeographicalReach:
    def __init__(self, geo_reach_dict):
        self.uri = geo_reach_dict['_uri']
        self.rdf_type = geo_reach_dict['rdf_type']
        self.rdfs_label = LangString(geo_reach_dict['rdfs_label'])


class LangString:
    def __init__(self, lang_string_dict):
        self.value = lang_string_dict['value']
        self.lang = lang_string_dict['lang']
    
    def dump(self):
        print("LangString: ")
        print("value: ", self.value)
        print("lang: ", self.lang)

class Offer:
    def __init__(self, offer_dict):
        self.uri = offer_dict['_uri']
        self.rdf_type = offer_dict['rdf_type']
        self.schema_price_spec = offer_dict['schema_priceSpecification']
        self.accepted_payment = offer_dict['schema_acceptedPaymentMethod']

class PeopleAudience:
    def __init__(self, audience_dict):
        self.uri = audience_dict['_uri']
        self.rdf_type = audience_dict['rdf_type']
        self.required_min_person = audience_dict['requiredMinPersonCount']
        self.required_max_person = audience_dict['requiredMaxPersonCount']
        self.suggested_gender = audience_dict['schema_suggestedGender'] #TODO change to correct class
        self.max_age = audience_dict['schema_requiredMaxAge']
        self.min_age = audience_dict['schema_suggestedMinAge']
        self.rdfs_label = audience_dict['rdfs_label']

class Period:
    def __init__(self, period_dict):
        self.uri = period_dict['_uri']
        self.rdf_type = period_dict['rdf_type']
        self.opening_details = LangString(period_dict['openingDetails'])
        self.applies_day = period_dict['appliesOnDay'] #TODO change to correct class
        self.start_time =  period_dict['startTime']
        self.end_date = period_dict['endDate'] #TODO change to correct class
        self.end_time = period_dict['endTime']
        self.week_month = period_dict['weekOfMonth']
        self.start_date = period_dict['startDate'] #TODO changpe to correct class

class Place:
    def __init__(self, place_dict):
        self.uri = place_dict['_uri']
        self.rdf_type = place_dict['rdf_type']
        self.schema_address = create_array_class(schema_PostalAddress, place_dict['schema_address'])
        self.schema_geo = create_array_class(schema_geocoordinates, place_dict['schema_geo'])
        self.open_hours = create_array_class(schema_Hours, place_dict['schema_openingHoursSpecification'])
        self.air_conditionning = place_dict['airConditioning']
        self.internet_access = place_dict['internetAccess']
        self.no_smoking = place_dict['noSmoking']
        self.altinsee = place_dict['altInsee']
        self.pets_allowed = place_dict['petsAllowed']

    def dump(self):
        print("uri: ", self.uri)
        print("rdf_type: ", self.rdf_type)
        print_array(self.schema_address)
        print_array(self.schema_geo)
        print_array(self.open_hours)
        print("air conditionning: ", self.air_conditionning)
        print("internet access: ", self.internet_access)
        print("no smoking: ", self.no_smoking)
        print("altinsee: ", self.altinsee)
        print("pets allowed: ", self.pets_allowed)

class PricingMode:
    def __init__(self, pricing_mode_dict):
        self.uri = pricing_mode_dict['_uri']
        self.rdf_type = pricing_mode_dict['rdf_type']
        self.rdfs_label = LangString(pricing_mode_dict['rdfs_label'])
    
class PricingOffer:
    def __init__(self, pricing_offer_dict):
        self.uri = pricing_offer_dict['_uri']
        self.rdf_type = pricing_offer_dict['rdf_type']
        self.rdfs_label = LangString(pricing_offer_dict['rdfs_label'])

class PricingPolicy:
    def __init__(self, pricing_policy_dict):
        self.uri = pricing_policy_dict['_uri']
        self.rdf_type = pricing_policy_dict['rdf_type']
        self.rdfs_label = LangString(pricing_policy_dict['rdfs_label'])

class PricingSeason:
    def __init__(self, pricing_season_dict):
        self.uri = pricing_season_dict['_uri']
        self.rdf_type = pricing_season_dict['rdf_type']
        self.rdfs_label = LangString(pricing_season_dict['rdfs_label'])

class Rating:
    def __init__(self, rating_dict):
        self.uri = rating_dict['_uri']
        self.rdf_type = rating_dict['rdf_type']
        self.review_system = rating_dict['isRatingProvidedBy'] #TODO change to correct class
        self.rdfs_label = rating_dict['rdfs_label']

class Region:
    def __init__(self, region_dict):
        self.uri = region_dict['_uri']
        self.rdf_type = region_dict['rdf_type']
        self.country = region_dict['isPartOfCountry'] #TODO change to correct class
        self.insee = region_dict['insee']
        self.rdfs_label = LangString(region_dict['rdfs_label'])

class Review:
    def __init__(self, review_dict):
        self.uri = review_dict['_uri']
        self.rdf_type = review_dict['rdf_type']
        self.reviews = review_dict['hasReviewValue']
        self.expiration_date = review_dict['reviewExpirationDate']
        self.review_creation_date = review_dict['reviewDeliveryDate']
        self.prending = review_dict['pending']
        self.published_date = review_dict['schema_datePublished']

class ReviewSystem:
    def __init__(self, review_system_dict):
        self.uri = review_system_dict['_uri']
        self.rdf_type = review_system_dict['rdf_type']
        self.validity_duration = review_system_dict['reviewValidityDuration']
        self.rdfs_label = LangString(review_system_dict['rdfs_label'])
        self.best_rating = review_system_dict['bestRating']
        self.worst_rating = review_system_dict['worstRating']

class RoomLayout:
    def __init__(self, room_dict):
        self.uri = room_dict['_uri']
        self.rdf_type = room_dict['rdf_type']
        self.rdfs_label = room_dict['rdfs_label']

class SpatialEnvTheme:
    def __init__(self, env_theme_dict):
        self.uri = env_theme_dict['_uri']
        self.rdf_type = env_theme_dict['rdf_type']
        self.rdfs_label = LangString(env_theme_dict['rdfs_label'])

class Theme:
    def __init__(self, theme_dict):
        self.uri = theme_dict['_uri']
        self.rdf_type = theme_dict['rdf_type']
        self.rdfs_label = create_array_class(LangString, theme_dict['rdfs_label'])

class TourPath:
    def __init__(self, tour_path_dict):
        self.uri = tour_path_dict['_uri']
        self.rdf_type = tour_path_dict['rdf_type']
        self.dc_description = tour_path_dict['dc_description']
        self.rdfs_label = tour_path_dict['rdfs_label']
        self.location = tour_path_dict['isLocatedAt']
        self.main_representation = tour_path_dict['hasMainRepresentation']
        self.audience = tour_path_dict['hasHikeAudience']
        self.representation = tour_path_dict['hasRepresentation']
        self.min_altitude = tour_path_dict['minAltitude']
        self.max_altitude = tour_path_dict['maxAltitude']
        self.tour_distance = tour_path_dict['tourDistance']
        self.duration = tour_path_dict['duration']
        self.high_difference = tour_path_dict['highDifference']

class TourType:
    def __init__(self, tour_type_dict):
        self.uri = tour_type_dict['_uri']
        self.rdf_type = tour_type_dict['rdf_type']
        self.rdfs_label = LangString(tour_type_dict['rdfs_label'])

class ebucore_Annotation:
    def __init__(self, annotation_dict):
        self.uri = annotation_dict['_uri']
        self.rdf_type = annotation_dict['rdf_type']
        self.comments = LangString(annotation_dict['ebucore_comments'])
        self.abstract = LangString(annotation_dict['ebucore_abstract'])
        self.credits = annotation_dict['credits']
        self.title = annotation_dict['ebucore_title']
        self.audience = annotation_dict['isDedicatedTo']
        self.start_date = annotation_dict['rightsStartDate']
        self.end_date = annotation_dict['rightsEndDate']

class ebucore_EditorialObject:
    def __init__(self, editorial_dict):
        self.uri = editorial_dict['_uri']
        self.rdf_type = editorial_dict['rdf_type']
        self.annotation = editorial_dict['ebucore_hasAnnotation']
        self.resource = editorial_dict['ebucore_hasRelatedResource']

class ebucore_mimetype:
    def __init__(self, mime_dict):
        self.uri = mime_dict['_uri']
        self.rdf_type = mime_dict['rdf_type']
        self.rdfs_label = mime_dict['rdfs_label']

class ebucore_resource:
    def __init__(self, resource_dict):
        self.uri = resource_dict['_uri']
        self.rdf_type = resource_dict['rdf_type']
        self.mime = resource_dict['ebucore_hasMimeType']
        self.width_unit = resource_dict['ebucore_widthUnit']
        self.locator = resource_dict['ebucore_locator']
        self.width = resource_dict['ebucore_width']
        self.heightUnit = resource_dict['ebucore_heightUnit']
        self.file_size = resource_dict['ebucore_fileSize']
        self.height = resource_dict['ebucore_height']

class oloSlot:
    def __init__(self, olo_slot_dict):
        self.uri = olo_slot_dict['_uri']
        self.rdf_type = olo_slot_dict['rdf_type']
        self.olo_item = olo_slot_dict['olo_item']
        self.olo_index = olo_slot_dict['olo_index']

class Contry:
    def __init__(self, country_dict):
        self.uri = country_dict['_uri']
        self.rdf_type = country_dict['rdf_type']
        self.rdfs_label = LangString(country_dict['rdfs_label'])

class schema_DayWeek:
    def __init__(self, schema_dayweek_dict):
        self.uri = schema_dayweek_dict['_uri']
        self.rdf_type = schema_dayweek_dict['rdf_type']
        self.rdfs_label = create_array_class(LangString , schema_dayweek_dict['rdfs_label'])
    
    def dump(self):
        print("uri: ", self.uri)
        print("rdf_type: ", self.rdf_type)
        print_array(self.rdfs_label)

class schema_Gender:
    def __init__(self, schema_gender):
        self.uri = schema_gender['_uri']
        self.rdf_type = schema_gender['rdf_type']
        self.rdfs_label = schema_gender['rdfs_label']

class schema_geocoordinates:
    def __init__(self, schema_geocoordinates):
        self.uri = schema_geocoordinates['_uri']
        self.rdf_type = schema_geocoordinates['rdf_type']
        self.longitude = schema_geocoordinates['schema_longitude']
        self.elevation = schema_geocoordinates['schema_elevation']
        self.latitude = schema_geocoordinates['schema_latitude']
        self.line = schema_geocoordinates['schema_line']
        self.polygon = schema_geocoordinates['schema_polygon']
        self.circle = schema_geocoordinates['schema_circle']
        self.box = schema_geocoordinates['schema_box']
    
    def dump(self):
        print("uri: ", self.uri)
        print("rdf_type: ", self.rdf_type)
        print("longitude: ", self.longitude)
        print("elevation: ", self.elevation)
        print("latitude: ", self.latitude)
        print("line: ", self.line)
        print("polygon: ", self.polygon)
        print("circle: ", self.circle)
        print("box: ", self.box)

class schema_Hours:
    def __init__(self, hours_dict):
        self.uri = hours_dict['_uri']
        self.rdf_type = hours_dict['rdf_type']
        self.days = create_array_class(schema_DayWeek, hours_dict['schema_dayOfWeek'])
        self.closes = hours_dict['schema_closes']
        self.add_info = create_array_class(LangString, hours_dict['additionalInformation'])
        self.end_period = hours_dict['schema_validThrough']
        self.start_period = hours_dict['schema_validFrom']
        self.open_hours = hours_dict['schema_opens']
        self.week_month = hours_dict['weekOfMonth']
    
    def dump(self):
        print("uri: ", self.uri)
        print("rdf_type: ", self.rdf_type)
        print_array(self.days)
        print("closes: ", self.closes)
        print_array(self.add_info)
        print("end period: ", self.end_period)
        print("start period: ", self.start_period)
        print("open hours: ", self.open_hours)
        print("week month: ", self.week_month)

class schema_PaymentMethod:
    def __init__(self, payment_method_dict):
        self.uri = payment_method_dict['_uri']
        self.rdf_type = payment_method_dict['rdf_type']
        self.rdfs_label = LangString(payment_method_dict['rdfs_label'])

class schema_PostalAddress:
    def __init__(self, postal_address_dict):
        self.uri = postal_address_dict['_uri']
        self.rdf_type = postal_address_dict['rdf_type']
        self.city = postal_address_dict['schema_addressLocality'][0]
        self.postal_code = postal_address_dict['schema_postalCode'][0]
        self.address = postal_address_dict['schema_streetAddress']
        self.box_number = postal_address_dict['schema_postOfficeBoxNumber']
        self.cedex = postal_address_dict['cedex']
    
    def dump(self):
        print("uri: ", self.uri)
        print("rdf_type: ", self.rdf_type)
        print('city: ', self.city)
        print("postal_code: ", self.postal_code)
        print("address: ", self.address)
        print("box_number: ", self.box_number)
        print("cedex: ", self.cedex)

class schema_priceSpecification:
    def __init__(self, price_spec_dict):
        self.uri = price_spec_dict['_uri']
        self.rdf_type = price_spec_dict['rdf_type']
        self.quantity = price_spec_dict['schema_eligibleQuantity']
        self.max_price = price_spec_dict['schema_maxPrice']
        self.name = LangString(price_spec_dict['name'])
        self.currency = price_spec_dict['schema_priceCurrency']
        self.add_info = price_spec_dict['additionalInformation']
        self.price = price_spec_dict['schema_price']
        self.min_price = price_spec_dict['schema_minPrice']
        self.periods = price_spec_dict['appliesOnPeriod']
        self.price_policy = price_spec_dict['hasEligiblePolicy']
        self.pricing_season = PricingSeason(price_spec_dict['hasPricingSeason'])
        self.audience = PeopleAudience(price_spec_dict['hasEligibleAudience'])
        self.pricing_mode = PricingMode(price_spec_dict['hasPricingMode'])
        self.offers = PricingOffer(price_spec_dict['hasPricingOffer'])

class schema_quantitativeValue:
    def __init__(self, quantitative_value):
        self.uri = quantitative_value['_uri']
        self.rdf_type = quantitative_value['rdf_type']
        self.min_value = quantitative_value['schema_minValue']
        self.unit = quantitative_value['schema_unitText']
        self.value = quantitative_value['schema_value']
        self.max_value = quantitative_value['schema_maxValue']

def create_array_class(className, data):
    res = []
    for elt in data:
        res.append(className(elt))
    return res

def print_array(array):
    for elt in array:
        elt.dump()


class POI:
    def __init__(self, poi_dict):
        self.uri = poi_dict['_uri']
        self.rdf_type = poi_dict['rdf_type']
        self.rdfs_comment = create_array_class(LangString, poi_dict['rdfs_comment'])
        self.rdfs_label = create_array_class(LangString, poi_dict['rdfs_label'])
        self.location = create_array_class(Place, poi_dict['isLocatedAt'])
        self.booking_contact = create_array_class(Agent, poi_dict['hasBookingContact'])
        self.suggests = None # TODO Fill this later
        self.features = create_array_class(Feature, poi_dict['hasFeature'])
        self.themes = create_array_class(Theme, poi_dict['hasTheme'])
        self.has_part = None # TODO Fill this later
        self.offers = create_array_class(Offer, poi_dict['offers'])
        self.communication_contact = create_array_class(Agent, poi_dict['hasCommunicationContact'])
        self.referenced_by = None # TODO Fill this later
        self.reviews = create_array_class(Review, poi_dict['hasReview'])
        self.owned_by = create_array_class(Agent, poi_dict['isOwnedBy'])
        self.managment_contact = create_array_class(Agent, poi_dict['hasManagementContact'])
        self.description = create_array_class(Description, poi_dict['hasDescription'])
        self.main_representation = create_array_class(ebucore_EditorialObject, poi_dict['hasMainRepresentation'])
        self.created_by = create_array_class(Agent, poi_dict['hasBeenCreatedBy'])
        self.equipped_with = create_array_class(Amenity, poi_dict['isEquippedWith'])
        self.neighbor = create_array_class(SpatialEnvTheme, poi_dict['hasNeighborhood'])
        self.geo_reach = create_array_class(GeographicalReach, poi_dict['hasGeographicReach'])
        self.representation = create_array_class(ebucore_EditorialObject, poi_dict['hasRepresentation'])
        self.contacts = create_array_class(Agent, poi_dict['hasContact'])
        self.published_by = create_array_class(Agent, poi_dict['hasBeenPublishedBy'])
        self.target = create_array_class(PeopleAudience, poi_dict['hasClientTarget'])
        self.administrative_contact = create_array_class(Agent, poi_dict['hasAdministrativeContact'])
        self.last_update = poi_dict['lastUpdate']
        self.allowed_persons = poi_dict['allowedPersons']
        self.available_lang = poi_dict['availableLanguage']
        self.reduced_mobility_access = poi_dict['reducedMobilityAccess']
        self.covid_open = poi_dict['COVID19OpeningPeriodsConfirmed']
        self.creation_date = poi_dict['creationDate']
        self.dc_identifier = poi_dict['dc_identifier']
        self.meets = None # TODO Fill this later
        self.min_alt = poi_dict['minAltitude']
        self.max_alt = poi_dict['maxAltitude']
        self.tour_distance = poi_dict['tourDistance']
        self.duration = poi_dict['duration']
        self.high_differences = poi_dict['highDifference']
        self.olo_slot = create_array_class(oloSlot, poi_dict['olo_slot'])
        self.consumable_for = None # TODO Fill this later
        self.architectural_style = create_array_class(ArchitecturalStyle, poi_dict['hasArchitecturalStyle'])
        self.cuisine_type = create_array_class(CuisineCategory, poi_dict['providesCuisineOfType'])
        self.take_away = poi_dict['takeAway']
        self.can_eat = poi_dict['allYouCanEat']
        self.food_products = create_array_class(FoodProduct, poi_dict['providesFoodProduct'])
        self.guided = poi_dict['guided']
        self.floor_size = create_array_class(schema_quantitativeValue, poi_dict['hasFloorSize'])
        self.sale_on_site = poi_dict['saleOnSite']

    
    def dump(self):
        print("Record: " + self.uri)
        print('\t', end='')
        print("uri: ", self.uri)
        print("\trdf_type: ", self.rdf_type)
        print_array(self.rdfs_comment)
        print_array(self.rdfs_label)
        print_array(self.location)

from_index = 0

query = """ """


def change_query():
    return """
    {
    poi(size: 100, from: """ + str(from_index) + """) {
        results {
        _uri
        rdf_type
        rdfs_comment {
            value
            lang
        }
        isLocatedAt {
            _uri
            rdf_type
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        lang
                        value
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            schema_geo {
            _uri
            rdf_type
            schema_longitude
            schema_elevation
            schema_latitude
            schema_line
            schema_polygon
            schema_circle
            schema_box
            }
            schema_openingHoursSpecification {
            _uri
            rdf_type
            schema_dayOfWeek {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            schema_closes
            additionalInformation {
                value
                lang
            }
            schema_validFrom
            schema_validThrough
            schema_opens
            weekOfMonth
            }
            airConditioning
            internetAccess
            noSmoking
            altInsee
            petsAllowed
        }
        rdfs_label {
            value
            lang
        }
        hasBookingContact {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        hasFeature {
            _uri
            rdf_type
            features {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            availableLanguage
            }
            charged
            schema_minValue
            schema_value
            schema_maxValue
            hasFloorSize {
            _uri
            rdf_type
            schema_minValue
            schema_unitText
            schema_value
            schema_maxValue
            }
            hasLayout {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            occupancy
            airConditioning
            seatCount
            internetAccess
            noSmoking
            petsAllowed
        }
        hasTheme {
            _uri
            rdf_type
            rdfs_label {
            value
            lang
            }
        }
        offers {
            _uri
            rdf_type
            schema_priceSpecification {
            _uri
            rdf_type
            schema_eligibleQuantity
            schema_maxPrice
            name {
                lang
                value
            }
            schema_priceCurrency
            additionalInformation {
                lang
                value
            }
            schema_price
            schema_minPrice
            appliesOnPeriod {
                _uri
                rdf_type
                openingDetails {
                value
                lang
                }
                appliesOnDay {
                _uri
                rdf_type
                rdfs_label {
                    value
                    lang
                }
                }
                startTime
                endDate
                endTime
                weekOfMonth
                startDate
            }
            hasEligiblePolicy {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            hasPricingSeason {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            hasEligibleAudience {
                _uri
                rdf_type
                requiredMinPersonCount
                requiredMaxPersonCount
                schema_suggestedGender {
                _uri
                rdf_type
                rdfs_label {
                    value
                    lang
                }
                }
                schema_requiredMaxAge
                schema_suggestedMinAge
                schema_suggestedMaxAge
                schema_requiredGender {
                _uri
                rdf_type
                rdfs_label {
                    value
                    lang
                }
                }
                schema_requiredMinAge
                rdfs_label {
                value
                lang
                }
            }
            hasPricingMode {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            hasPricingOffer {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            }
            schema_acceptedPaymentMethod {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
        }
        hasCommunicationContact {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        hasReview {
            _uri
            rdf_type
            hasReviewValue {
            _uri
            rdf_type
            isRatingProvidedBy {
                _uri
                rdf_type
                reviewValidityDuration
                rdfs_label {
                value
                lang
                }
                bestRating
                worstRating
                rdfs_label {
                value
                lang
                }
            }
            rdfs_label {
                value
                lang
            }
            }
            reviewExpirationDate
            reviewDeliveryDate
            pending
            schema_datePublished
        }
        isOwnedBy {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        hasManagementContact {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        hasDescription {
            _uri
            rdf_type
            dc_description {
            value
            lang
            }
            isDedicatedTo {
            _uri
            rdf_type
            requiredMinPersonCount
            requiredMaxPersonCount
            schema_suggestedGender {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            schema_requiredMaxAge
            schema_suggestedMinAge
            schema_suggestedMaxAge
            schema_requiredGender {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            schema_requiredMinAge
            rdfs_label {
                value
                lang
            }
            }
            shortDescription {
            value
            lang
            }
        }
        hasMainRepresentation {
            _uri
            rdf_type
            ebucore_hasAnnotation {
            _uri
            rdf_type
            ebucore_comments {
                value
                lang
            }
            ebucore_abstract {
                value
                lang
            }
            credits
            ebucore_title {
                value
                lang
            }
            ebucore_isCoveredBy
            isDedicatedTo {
                _uri
                rdf_type
                requiredMinPersonCount
                requiredMaxPersonCount
                schema_suggestedGender {
                _uri
                rdf_type
                rdfs_label {
                    value
                    lang
                }
                }
                schema_requiredMaxAge
                schema_suggestedMinAge
                schema_suggestedMaxAge
                schema_requiredGender {
                _uri
                rdf_type
                rdfs_label {
                    value
                    lang
                }
                }
                schema_requiredMinAge
                rdfs_label {
                value
                lang
                }
            }
            rightsStartDate
            dct_hasVersion
            rightsEndDate
            }
            ebucore_hasRelatedResource {
            _uri
            rdf_type
            ebucore_hasMimeType {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            ebucore_widthUnit
            ebucore_locator
            ebucore_width
            ebucore_heightUnit
            ebucore_fileSize
            ebucore_height
            }
        }
        hasBeenCreatedBy {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        isEquippedWith {
            _uri
            rdf_type
            rdfs_label {
            value
            lang
            }
            availableLanguage
        }
        hasNeighborhood {
            _uri
            rdf_type
            rdfs_label {
            value
            lang
            }
        }
        hasGeographicReach {
            _uri
            rdf_type
            rdfs_label {
            value
            lang
            }
        }
        hasRepresentation {
            _uri
            rdf_type
            ebucore_hasAnnotation {
            _uri
            rdf_type
            ebucore_comments {
                value
                lang
            }
            ebucore_abstract {
                value
                lang
            }
            credits
            ebucore_title {
                value
                lang
            }
            ebucore_isCoveredBy
            isDedicatedTo {
                _uri
                rdf_type
                requiredMinPersonCount
                requiredMaxPersonCount
                schema_suggestedGender {
                _uri
                rdf_type
                rdfs_label {
                    value
                    lang
                }
                }
                schema_requiredMaxAge
                schema_suggestedMinAge
                schema_suggestedMaxAge
                schema_requiredGender {
                _uri
                rdf_type
                rdfs_label {
                    value
                    lang
                }
                }
                schema_requiredMinAge
                rdfs_label {
                value
                lang
                }
            }
            rightsStartDate
            dct_hasVersion
            rightsEndDate
            }
            ebucore_hasRelatedResource {
            _uri
            rdf_type
            ebucore_hasMimeType {
                _uri
                rdf_type
                rdfs_label {
                value
                lang
                }
            }
            ebucore_widthUnit
            ebucore_locator
            ebucore_width
            ebucore_heightUnit
            ebucore_fileSize
            ebucore_height
            }
        }
        hasContact {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        hasBeenPublishedBy {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        hasClientTarget {
            _uri
            rdf_type
            requiredMinPersonCount
            requiredMaxPersonCount
            schema_suggestedGender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_requiredMaxAge
            schema_suggestedMinAge
            schema_suggestedMaxAge
            schema_requiredGender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_requiredMinAge
            rdfs_label {
            value
            lang
            }
        }
        hasAdministrativeContact {
            _uri
            rdf_type
            rdfs_comment {
            value
            lang
            }
            schema_address {
            _uri
            rdf_type
            schema_addressLocality
            schema_postalCode
            schema_streetAddress
            schema_postOfficeBoxNumber
            hasAddressCity {
                _uri
                rdf_type
                isPartOfDepartment {
                _uri
                rdf_type
                isPartOfRegion {
                    _uri
                    rdf_type
                    isPartOfCountry {
                    _uri
                    rdf_type
                    rdfs_label {
                        value
                        lang
                    }
                    }
                    insee
                    rdfs_label {
                    value
                    lang
                    }
                }
                insee
                rdfs_label {
                    value
                    lang
                }
                }
                insee
                rdfs_label {
                value
                lang
                }
            }
            cedex
            }
            foaf_homepage
            foaf_title
            schema_gender {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            schema_faxNumber
            schema_telephone
            schema_email
            schema_givenName
            schema_familyName
            agreementLicense
            registeredNumber
            siret
            apeNaf
            rcs
            schema_legalName
            schema_logo
        }
        lastUpdate
        allowedPersons
        lastUpdateDatatourisme
        availableLanguage
        reducedMobilityAccess
        COVID19OpeningPeriodsConfirmed
        creationDate
        dc_identifier
        COVID19SpecialMeasures {
            value
            lang
        }
        takesPlaceAt {
            _uri
            rdf_type
            openingDetails {
            value
            lang
            }
            appliesOnDay {
            _uri
            rdf_type
            rdfs_label {
                value
                lang
            }
            }
            startTime
            endDate
            endTime
            weekOfMonth
            startDate
        }
        hasTourType {
            _uri
            rdf_type
            rdfs_label {
            value
            lang
            }
        }
        minAltitude
        maxAltitude
        tourDistance
        duration
        highDifference
        olo_slot {
            _uri
            rdf_type
            olo_item {
            _uri
            rdf_type
            }
            olo_index
        }
        hasArchitecturalStyle {
            _uri
            rdf_type
            rdfs_label {
            value
            lang
            }
        }
        providesCuisineOfType {
            _uri
            rdf_type
            rdfs_label {
            value
            lang
            }
        }
        takeAway
        allYouCanEat
        providesFoodProduct {
            _uri
            rdf_type
            rdfs_label {
            lang
            value
            }
        }
        guided
        hasFloorSize {
            _uri
            rdf_type
            schema_minValue
            schema_unitText
            schema_value
            schema_maxValue
        }
        saleOnSite
        }
    }
    }
    """

mongo_client = MongoClient('localhost', 3999)
col = mongo_client.db.create_collection('datatourisme')

result = None
graphql_url = 'http://localhost:8080/'

query = change_query()

while True:
    variables = dict(from_index = from_index, after= None)
    r = requests.post(graphql_url, json={'query': query, 'variables': variables})
    result = r.json()
    if result['data']['poi']['results'] is []:
        break
    col.insert_many(result['data']['poi']['results'])
    print("from_index", from_index)
    from_index += 100
    query = change_query()
