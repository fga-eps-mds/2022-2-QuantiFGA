//Tentando criar uma variável objeto para filtrar algumas coisas
let fga=[{
	uac:[{
		salas:[
		{
			idSala: "S1",
			capacidadeSala: "123",
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


