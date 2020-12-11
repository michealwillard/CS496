//
//  Pokeapi.swift
//  PokeapiDex
//
//  Created by Micheal Willard on 10/31/16.
//  Copyright © 2016 Twilio. All rights reserved.
//

import Foundation
import Siesta
import SwiftyJSON

let Pokeapi = _Pokeapi()

class _Pokeapi: Service {
    /*private*/
    init() {
        super.init(baseURL: "https://pokeapi.co/api/v2")
        
        // Configuration
        self.configure {
            //$0.config.pipeline[.parsing].add(SwiftyJSONTransformer, contentTypes: ["*/json"])
            //$0.config.expirationTime = 3600
            $0.pipeline[.parsing].add(SwiftyJSONTransformer, contentTypes: ["*/json"])
            $0.expirationTime = 3600
        }
        
        self.configureTransformer("/pokemon") {
            ($0.content as JSON)["results"].arrayValue
        }
    }
    var pokedex: Resource { return resource("/pokemon").withParam("limit", "151") }
}

private let SwiftyJSONTransformer =
    ResponseContentTransformer
        { JSON($0.content as AnyObject) }



