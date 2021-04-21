import requests
import json
import pandas as pandas

query = """
{
  poi(size: 1) {
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

url = 'http://localhost:8080/'
r = requests.post(url, json={'query': query})

f = open("result.json", "w")

if r.status_code == 200:
  f.write(json.dumps(r.json(), indent=2))
f.close()
