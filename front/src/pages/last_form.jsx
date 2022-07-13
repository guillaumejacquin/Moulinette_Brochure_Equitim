
import "./last_form.css";
import { useState, useEffect } from 'react';
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";

import FormControl from '@mui/material/FormControl';

import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';



const Last_form = () => {
    const [Nom, setNom] = useState('')
    const [Typologie, setTypologie] = useState('')
    const [Droit_applicable, setDroit] = useState('')
    const [Isin, setISIN] = useState('')
    const [Emission, setEmission] = useState('')
    const [DCI, setDCI] = useState('')
    const [DR1, setDR1] = useState('')
    const [DPR, setDPR] = useState('')
    const [DADR, setDADR] = useState('')
    const [DCF, setDCF] = useState('')
    const [DEC, setDEC] = useState('')
    const [ADCF, setADCF] = useState('')
    const [F0, setF0] = useState('')
    const [TSJ, setTSJ] = useState('')
    const [DDP, setDDP] = useState('')
    const [PCS1, setPCS1] = useState('')
    const [PCS2, setPCS2] = useState('')
    const [PCS3, setPCS3] = useState('')
    const [PCS4, setPCS4] = useState('')
    const [PCS5, setPCS5] = useState('')
    const [CPN, setCPN] = useState('')
    const [CPN_is_memoire, setCPN_is_memoire] = useState('')
    const [PDI, setPDI] = useState('')
    const [BAC, setBAC] = useState('')
    const [BAC_is_degressif, setBAC_is_degressif] = useState('')
    const [BCPN, setBCPN] = useState('')
    const [BCPN_is_degressif, setBCPN_is_degressif] = useState('')

    const [COM, setCOM] = useState('')
    const [NSD, setNSD] = useState('')
    const [NSM, setNSM] = useState('')
    const [NSF, setNSF] = useState('')
    const [ABDAC, setABDAC] = useState('')
    const [DBAC, setDBAC] = useState('')
    const [DEG, setDEG] = useState('')
    const [type_strike, settype_strike] = useState('')
    const [type_bar, settype_bar] = useState('')
    const [sous_jacent, setsous_jacent] = useState('')
    const [template, settemplate] = useState('')
    const [type_bar2, settype_bar2 ] = useState('')
    const [loading, setLoading] = useState(false)
    const [jdr, setjdr] = useState('')

    const [response, setResponse] = useState("")
    const [buttonisclicked, setbuttonisclicked] = useState("")

    const [NJO, setNJO] = useState("")


    const menu_déroulant = (template, settemplate) => {
      const names = ['BNP Paribas', "Crédit Suisse", "Société Générale", "Goldman Sachs FCI", "Morgan Stanley", "Goldman Sachs International", "Natixis"]
      
      function importAll(r) {
        return r.keys().map(r);
      }
      
      const images = importAll(require.context('../../../Templates', true, /\.pptx/));
      
      return (
        <div style={{marginLeft:"-5%", marginTop:"2%"}}>
        {/* <ul>{listItems}</ul> */}


    <FormControl>
        <InputLabel id="template">Template</InputLabel>

        <Select
              labelId="template"
              sx={{ minWidth: 200 }}

              id="template"
              value={template}
              label="template"
              onChange={(e)=>settemplate(e.target.value)}
              >
              
              {names.map(images => <MenuItem value={images}>{images}</MenuItem>)}
    
    
            </Select> 
            </FormControl>

        </div>
      );
    }

    const first_bloc = () => {
        return(
            <div className="text_rec">
                <div className="column1">
                    <TextField label="Nom du produit <nom>" name="Nom"
                        style={{width:"30%"}}
                        onChange={(e)=>setNom(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>

                    <TextField
                        style={{width:"30%"}}
                        label="ISIN <ISIN>"
                        name="Isin"
                        inputProps={{ maxLength: 12 }}

                        onChange={(e)=>setISIN(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>

                        <FormControl>

                        <InputLabel style={{marginTop:"7%", marginLeft:"5%"}}id="Droit">Droit</InputLabel>
                                <Select
                                style={{marginTop:"7%"}}
                                sx={{ m: 1, minWidth: 200 }}
                                labelId="Droit"
                                id="Droit"
                                value={Droit_applicable}
                                label="Droit"
                                onChange={(e)=>setDroit(e.target.value)}
                                >
                                <MenuItem value={"français"}>Français</MenuItem>
                                <MenuItem value={"anglais"}>Anglais</MenuItem>
                                <MenuItem value={"suisse"}>Suisse</MenuItem>
                                </Select>
                        </FormControl>
                        
                </div>
 
                <div className="column1">
                
                  <TextField
                        style={{width:"30%"}}
                        label="Emission <Emission>"
                        name="Emission"
                        onChange={(e)=>setEmission(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                
                <TextField
            label="Commission"
            style={{width:"30%", marginTop:"2%", marginLeft:"-1.5%"}}
            name="COM"
            onChange={(e)=>setCOM(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />
            <div style={{marginLeft:"0%", marginTop:"1.4%"}}>                                   
              {menu_déroulant(template, settemplate)}
            </div>
     
            </div>
            
            </div>
        );
    }
    const third_bloc = () => {
        return(
            <div className="text_rec">
                <div className="thirdbloc">
                    <div className="thirdbloctitle" style={{marginLeft:"1%"}}>
                        <div className="thirdblocrealtitle" style={{marginLeft:"0%"}}> Dates Constatation & Paiement</div>
                        <div>
                            <TextField
                                style={{width:"80%", marginLeft:"1.8%", marginTop:"10%"}}

                                label="Date(s) de constatation(s) initiale(s)"
                                name="DCI"
                                onChange={(e)=>setDCI(e.target.value)}
                                margin="normal"
                                variant="outlined"
                                autoComplete="on"
                                fullWidth/>
                        </div>
                        <TextField
                        style={{width:"80%", marginLeft:"1.8%"}}
                        label="Date de premier rappel"
                        name="Date de premier rappel"
                        onChange={(e)=>setDPR(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                        
                        <TextField
                        style={{width:"80%", marginLeft:"1.8%"}}
                        label="Avant dernière date de constatation"
                        name="Avant dernière date de constatation"
                        onChange={(e)=>setADCF(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>


                        <TextField
                        style={{width:"80%", marginLeft:"1.8%"}}
                        label="Date de constatation finale"
                        name="Date de constatation finale"
                        onChange={(e)=>setDCF(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                    </div>
                    
                    
                    <div className="thirdbloctitle" style={{marginLeft:"1%"}}>
                        <div style={{width:"80%", marginLeft:"0%", marginTop:"14.55%"}}>
                        <FormControl>
                            <InputLabel style={{marginTop:"0%"}}id="Type de strike">Type de strike</InputLabel>
                            <Select
                                sx={{  minWidth: 200 }}

                                labelId="type_strike"
                                id="type_strike"
                                value={type_strike}
                                label="type_strike"
                                onChange={(e)=>settype_strike(e.target.value)}
                                >
                                <MenuItem value={"strike normal"}>Strike normal</MenuItem>
                                <MenuItem value={"strike moyen"}>Strike moyen</MenuItem>
                                <MenuItem value={"best strike"}>Best strike</MenuItem>
                            </Select>
                        </FormControl>
                        </div>
                        
                       <TextField
                        style={{width:"80%", marginLeft:"0.6%", marginTop:"9%"}}
                        label="Date de remboursement premier rappel"
                        name="Date de remboursement premier rappel"
                        onChange={(e)=>setDR1(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                              
                        <TextField
                        style={{width:"80%", marginLeft:"0.6%"}}
                        label="Avant dernière date de remboursement"
                        name="Avant dernière date de remboursement"
                        onChange={(e)=>setDADR(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>

                        <TextField
                        style={{width:"80%", marginLeft:"0.6%"}}
                        label="Date d'échéance"
                        name="Date d'échéance"
                        onChange={(e)=>setDEC(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                    
                    </div>
                    <div className="thirdbloctitle" style={{marginLeft:"1%"}}>
                        <div className="thirdblocrealtitle" style={{marginLeft:"10%"}}>Génération de dates</div>
                        <div>
                            <TextField
                            style={{width:"80%", marginLeft:"0%", marginTop:"25%"}}
                            label="Jour de référence <pasfait>"
                            name="Jdr"
                            onChange={(e)=>setjdr(e.target.value)}
                            margin="normal"
                            variant="outlined"
                            autoComplete="on"
                            fullWidth/>
                        </div>
                        <div>
                            <TextField
                            style={{width:"80%", marginLeft:"0%", marginTop:"25%"}}
                            label="Nombre de jours ouvrés"
                            name="NJO"
                            onChange={(e)=>setNJO(e.target.value)}
                            margin="normal"
                            variant="outlined"
                            autoComplete="on"
                            fullWidth
                          />
                        </div>
                    </div>             

                    <div className="thirdbloctitle" style={{marginLeft:"1%"}}>
                        <div className="thirdblocrealtitle" style={{marginLeft:"10%"}}>Scénarios</div>
                        <div>
                            <TextField
                            style={{width:"80%", marginLeft:"0%", marginTop:"10%"}}
                            label="Niveau de scénario défavorable"
                            name="NSD"
                            onChange={(e)=>setNSD(e.target.value)}
                            margin="normal"
                            variant="outlined"
                            autoComplete="on"
                            fullWidth/>
                        </div>
                        <div>
                            <TextField
                            style={{width:"80%", marginLeft:"0%", marginTop:"10%"}}
                            label="Niveau de scénario médian"
                            name="NSM"
                            onChange={(e)=>setNSM(e.target.value)}
                            margin="normal"
                            variant="outlined"
                            autoComplete="on"
                            fullWidth/>
                        </div>
                        <div>
                            <TextField
                            style={{width:"80%", marginLeft:"0%", marginTop:"10%"}}
                            label="Niveau de scénario favorable"
                            name="NSF"
                            onChange={(e)=>setNSF(e.target.value)}
                            margin="normal"
                            variant="outlined"
                            autoComplete="on"
                            fullWidth/>
                        </div>
                    </div>
                    </div>
            </div>
        );
    }

    const handleSubmit  = (event) => {
        event.preventDefault();
  
      // Simple POST request with a JSON body using fetch
      
      const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ 
            Nom: Nom, Typologie:Typologie,
            Droit: Droit_applicable, Isin: Isin, Emission:Emission, DCI:DCI,
            DR1:DR1, DPR:DPR, DADR:DADR, DCF:DCF, DEC:DEC, ADCF:ADCF,
            F0:F0, TSJ:TSJ, PCS1:PCS1, PCS2:PCS2, PCS3:PCS3, PCS4:PCS4, PCS5:PCS5,
            CPN:CPN, CPN_is_memoire:CPN_is_memoire, PDI:PDI, 
            BAC:BAC, BAC_is_degressif:BAC_is_degressif, BCPN:BCPN, BCPN_is_degressif:BCPN_is_degressif,
             COM:COM, NSD:NSD, NSM:NSM, NSF:NSF,
            ABDAC:ABDAC, DBAC:DBAC, DEG:DEG, type_strike:type_strike,
            type_bar:type_bar, sous_jacent:sous_jacent, template:template, DDP:DDP, type_bar2:type_bar2, NJO:NJO, jdr:jdr
          })

          
      };
      // setLoading(true);
      let test = ""
      fetch('http://localhost:5000/add', requestOptions)
          .then(response => response.json())
          .then(response => test = (response))
          .then(console.log("response", response))
          .then(response => setResponse(response))
          .then(response => setbuttonisclicked("true"))

        }
    
    const second_bloc = () => {
        return(
            <div className="text_rec">
                <div className="column1">
                    
                <FormControl>

                    <InputLabel style={{marginTop:"7%"}}id="Typologie">Typologie</InputLabel>
                        <Select
                        style={{marginTop:"7%"}}
                        sx={{ m: 1, minWidth: 200 }}

                        labelId="Typologie"
                        id="Typologie"
                        value={Typologie}
                        label="Typologie"
                        onChange={(e)=>setTypologie(e.target.value)}
                        >
                        <MenuItem value={"coupon autocall"}>Coupon Autocall</MenuItem>
                        <MenuItem value={"coupon phoenix"}>Coupon Phoenix</MenuItem>
                        </Select> 
                    </FormControl>

                    <FormControl>
                        <InputLabel style={{marginTop:"5%" }}id="F0">Fréquence</InputLabel>
                        <Select
                            style={{marginTop:"7%"}}
                            sx={{ m: 1, minWidth: 200 }}
                            labelId="F0"
                            id="F0"
                            value={F0}
                            label="F0"
                            onChange={(e)=>setF0(e.target.value)}
                            >
                            <MenuItem value={"jours"}>Quotidienne</MenuItem>
                            <MenuItem value={"mois"}>Mensuelle</MenuItem>
                            <MenuItem value={"trimestre"}>Trimestrielle</MenuItem>
                            <MenuItem value={"semestre"}>Semestrielle</MenuItem>
                            <MenuItem value={"année"}>Annuelle</MenuItem>
                            </Select>
                    </FormControl>
    
                    <TextField
                        label="Coupon périodique (%)"
                        style={{width:"30%"}}

                        name="CPN"
                        onChange={(e)=>setCPN(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                        
                </div>
                <div className="column2">
                    <TextField
                    style={{width:"30%", marginLeft:"1%"}}

                    label="Sous-jacent(s)"
                    name="TSJ"
                    onChange={(e)=>setTSJ(e.target.value)}
                    margin="normal"
                    variant="outlined"
                    autoComplete="on"
                    fullWidth/>

                    <FormControl>
                        <InputLabel style={{marginTop:"5%", marginLeft:"20%" }}id="F0">Type de sous jacent</InputLabel>
                        <Select
                        labelId="sous_jacent"
                        style={{marginTop:"7%", marginLeft:"20%"}}
                        sx={{ m: 1, minWidth: 200 }}
                        id="sous_jacent"
                        value={sous_jacent}
                        label="sous_jacent"
                        onChange={(e)=>setsous_jacent(e.target.value)}
                        >
                        <MenuItem value={"mono action"}>Mono action</MenuItem>
                        <MenuItem value={"wo action"}>WO actions</MenuItem>
                        <MenuItem value={"equipondéré action"}>Equipondéré actions</MenuItem>
                        <MenuItem value={"mono indice"}>Mono indice</MenuItem>
                        <MenuItem value={"equipondéré indice"}>Equipondéré indices</MenuItem>
                        <MenuItem value={"wo indice"}>WO indices</MenuItem>
                        </Select> 
                    </FormControl>
                </div>

                <div className="column5">
                <div style={{marginTop:"2%", marginLeft:"1.5%", fontWeight: "bold", width:"17%"}}>Barrière de remboursement</div>
                    <TextField
                        style={{width:"15%", marginLeft:"4.7%"}}
                        label="Barrière de remboursement initiale"
                        name="BAC"
                        onChange={(e)=>setBAC(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                        
                        <div style={{width:"15%", marginLeft:"2%", marginTop:"1.1%"}}>
                            <FormControl>
                                <InputLabel style={{marginTop:"0%"}}id="Type de barrière">Type de barrière</InputLabel>
                                    <Select
                                        labelId="type_bar"
                                        sx={{minWidth: 200 }}

                                        id="type_bar"
                                        value={type_bar}
                                        label="type_bar"
                                        onChange={(e)=>settype_bar(e.target.value)}
                                        >
                                        <MenuItem value={"  "}>Dégressive</MenuItem>
                                        <MenuItem value={"airbag"}>Airbag</MenuItem>
                                        <MenuItem value={"normal"}>Normale</MenuItem>
                                    </Select> 

                            </FormControl>
                        </div>

                    <TextField
                        style={{width:"15%", marginLeft:"2%"}}
                        label="Pas de degressivité"
                        name="DEG"
                        onChange={(e)=>setDEG(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>

                    <TextField
                        style={{width:"15%", marginLeft:"2%"}}
                        label="Avant dernier niveau de barrière dégressive"
                        name="ABDAC"
                        onChange={(e)=>setABDAC(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                    <TextField
                        style={{width:"15%", marginLeft:"2%"}}
                        label="Dernier niveau de barrière dégressive/airbag"
                        name="DBAC"
                        onChange={(e)=>setDBAC(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                </div>

                <div className="column5">
                <div style={{marginTop:"2%", marginLeft:"1.5%", fontWeight: "bold", width:"17%"}}>Coupon phoenix</div>
                
                    <TextField
                        style={{width:"15%", marginLeft:"4.7%"}}
                        label="Barrière de coupon"
                        name="BCPN"
                        onChange={(e)=>setBCPN(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>

                        <div style={{width:"15%", marginLeft:"2%", marginTop:"1.1%"}}>
                            <FormControl>
                                <InputLabel style={{marginTop:"0%"}}id="Barrière de coupon dégressive">Barrière de coupon dégressive</InputLabel>
                                <Select
                                    sx={{minWidth: 200 }}
                                    labelId="BCPN_is_degressif"
                                    id="BCPN_is_degressif"
                                    value={BCPN_is_degressif}
                                    label="BCPN_is_degressif"
                                    onChange={(e)=>setBCPN_is_degressif(e.target.value)}
                                    >
                                    <MenuItem value={"oui"}>oui</MenuItem>
                                    <MenuItem value={"non"}>non</MenuItem>
                                </Select>
                            </FormControl>
                        </div>
                        
                  <TextField
                        style={{width:"15%", marginLeft:"1.8%"}}
                        label="Début dégressivité Phoenix"
                        name="Début dégressivité Phoenix"
                        onChange={(e)=>setDDP(e.target.value)}
                        margin="normal"
                        variant="outlined"
                        autoComplete="on"
                        fullWidth/>
                
                        <div style={{width:"15%", marginLeft:"2%", marginTop:"1.12%"}}></div>
                        <div style={{width:"15%", marginLeft:"2%", marginTop:"1.12%"}}></div>                
                </div>

                    <div className="protection">
                    <div style={{marginTop:"5%", marginLeft:"2%", fontWeight: "bold", width:"32%"}}></div>

                    <FormControl>
                    <InputLabel style={{marginTop:"7%", marginLeft:"8.6%"}}id="Barrière coupon mémoire">Barrière coupon mémoire</InputLabel>
                        <Select
                                style={{marginTop:"7%", marginLeft:"8.6%"}}
                                sx={{ m: 1, minWidth: 200 }}
                                labelId="CPN_is_memoire"
                                id="CPN_is_memoire"
                                value={CPN_is_memoire}
                                label="CPN_is_memoire"
                                onChange={(e)=>setCPN_is_memoire(e.target.value)}
                                >
                                <MenuItem value={"oui"}>oui</MenuItem>
                                <MenuItem value={"non"}>non</MenuItem>
                                </Select>
                    </FormControl>

                </div>
                
                <div className="protection">
                    <div style={{marginTop:"5%", marginLeft:"2%", fontWeight: "bold", width:"32%"}}>Protection</div>
                    <TextField
                            label="Barrière de protection"
                            style={{width:"21%", marginLeft:"2%"}}
                            name="PDI"
                            onChange={(e)=>setPDI(e.target.value)}
                            margin="normal"
                            variant="outlined"
                            autoComplete="on"
                            fullWidth/>
                    </div>
        </div>
        );
    }

    return (
    <div> 
        <h1> LA MOULINETTE BROCHURE </h1>
        <h3> INFORMATIONS GENERALES </h3>
        <div className="rect" style={{marginTop:"1.3%"}}>
            {first_bloc()}
        </div>
        
        <h3>STRUCTURE PRODUIT</h3>
        <div className="rect" style={{marginTop:"1.3%"}}>

            {second_bloc()}
        </div>
        <h3>DATES & SCENARIOS</h3>
        <div className="rect" style={{marginTop:"1.3%", marginBottom:"5%"}}>
        {third_bloc()}
        </div>

        <div>
        <Button 
       //#0B3371
          variant="contained"
            color="primary"
            size="large"
            style={{ marginTop: "0%", left:"40%", width:"20%", marginBottom:"3%", backgroundColor:"#0B3371", minHeight: '60px'}}
            onClick={handleSubmit}
          >
            Générer la brochure
          </Button>
          {/* {Error()} */}
        </div>
    </div>
    );
};

export default Last_form;
