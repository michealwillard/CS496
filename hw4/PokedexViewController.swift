//
//  PokedexViewController
//  PokeapiDex
//
//  Created by Brent Schooley on 8/3/16.
//  Copyright © 2016 Twilio. All rights reserved.
//

import UIKit
import SwiftyJSON
import Siesta

class PokedexViewController: UITableViewController, ResourceObserver {
    // MARK: - Resource code
    var pokedexResource: Resource? {
        didSet {
            oldValue?.removeObservers(ownedBy: self)
            
            pokedexResource?
                .addObserver(self)
                .addObserver(statusOverlay, owner: self)
                .loadIfNeeded()
        }
    }
    
    func resourceChanged(_ resource: Resource, event: ResourceEvent) {
        pokemonList = pokedexResource?.typedContent() ?? []
    }
    
    var statusOverlay = ResourceStatusOverlay()
    
    override func viewDidLayoutSubviews() {
        statusOverlay.positionToCoverParent()
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        statusOverlay.embedIn(self)
        pokedexResource = Pokeapi.pokedex
    }
    
    // Replace these with Pokemon!
    var pokemonList: [JSON] = [] {
        didSet {
            tableView.reloadData()
        }
    }
    
    // MARK: - View Lifecycle
    
    // MARK: - Table View
    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return pokemonList.count
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "PokemonCell", for: indexPath as IndexPath)
        
        // Get pokemon out of pokemon resource
        let pokemonSummary = pokemonList[indexPath.row]
        
        // Customize cell here based on pokemon
        cell.textLabel?.text = pokemonSummary["name"].stringValue.capitalizedString
        cell.detailTextLabel?.text = "id: \(indexPath.row + 1)"
        
        return cell
    }
    
    // MARK: - Segues
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "showDetail" {
            if let indexPath = self.tableView.indexPathForSelectedRow {
                
            }
        }
    }
    
}
