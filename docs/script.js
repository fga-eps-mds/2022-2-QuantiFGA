//Tentando criar uma variável objeto para filtrar algumas coisas
let fga=[{
	uac:[{
		salas:[
		{
			idSala: "S1",
			capacidadeSala: "500",
			rotinas:[
			{
			diaSemana: "Segunda-Feira",
			horarios:[
			{
			hora: "08:00",
			dadosDisciplina:[
			{
				nomeDisciplina: "C1",
				dptoDisciplina: "Matemática",
				doscenteDisciplina: "Rodrigo Cerda",
				vagasOfertadas:"120",
				vagasPreenchidas:"119",
			}
			]
			},
						{
			hora: "09:00",
			dadosDisciplina:[
			{
				nomeDisciplina: "Física 1",
				dptoDisciplina: "Física",
				doscenteDisciplina: "Lindomar",
				vagasOfertadas:"120",
				vagasPreenchidas:"9",
			}
			]
			}
			
			
			]
			
			}
			]
			
		}]
		}]
			}]
//fecha a variável objeto

preencherDados();

function preencherDados(){
	const dadosIniciais= document.querySelectorAll(".sala");

	let aux_uac = fga[0].uac[0].salas.length;

	let aux_ued;
	let aux_ltdea;
	let aux_conteiner;
	
	for (let i=0; i<aux_uac; i++){
		dadosIniciais[i].classList.add("adicionando-dados");

		let adicionandoInfos = document.querySelector(".adicionando-dados");

		let addNomeSala = document.querySelector(".adicionando-dados .numSala");
		let nomeSala = fga[0].uac[0].salas[i].idSala; 	
		addNomeSala.innerHTML=`${nomeSala}` ;

		let addCapacidadeSala = document.querySelector(".adicionando-dados .capacidadeSala");
		let capacidadeSala = fga[0].uac[0].salas[i].capacidadeSala
		addCapacidadeSala.innerHTML=`${capacidadeSala}🪑` ;
		
		// let addOcupacaoSala = document.querySelector(".adicionando-dados .porta .meiaPorta.superior .taxaOcupacao")
		

		// dadosIniciais[i].classList.remove("adicionando-dados")
		// console.log(dadosIniciais[i]);
		
		// adicionandoInfos = document.querySelector(".adicionando-dados")
		// console.log(adicionandoInfos + " Esse valor deve ser null");

	}

}


function infoSala(sala){
    const dadosSala = document.querySelector(".sala.sala-selecionada");

    if (dadosSala!=null){
    dadosSala.classList.remove("sala-selecionada");
    sala.classList.add("sala-selecionada");
    } else {
        sala.classList.add("sala-selecionada");
    }
    
    popUpsala();

}

function  popUpsala (){

const taxaOcupacaoLivre = document.querySelector(".sala-selecionada .meiaPorta.superior");
let percentilVagas = 100*(Number(fga[0].uac[0].salas[0].rotinas[0].horarios[1].dadosDisciplina[0].vagasPreenchidas)/Number(fga[0].uac[0].salas[0].rotinas[0].horarios[1].dadosDisciplina[0].vagasOfertadas));
taxaOcupacaoLivre.innerHTML= `${percentilVagas}%`;


const taxaOcupacaoIndisponivel = document.querySelector(".sala-selecionada .meiaPorta.inferior");
const taxaOcupacao=[taxaOcupacaoLivre, taxaOcupacaoIndisponivel]
console.log(taxaOcupacao);
}


