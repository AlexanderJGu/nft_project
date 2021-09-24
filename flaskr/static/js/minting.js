var simpleMarketplace_instance = new window.web3.eth.Contract(simpleMarketplace_abi, simpleMarketplace_address);





async function updatePage(){

  let minted = document.querySelector('#adopted')



  let maxSupply = await simpleMarketplace_instance.methods.maxToMint().call()



  let totalSupply = await simpleMarketplace_instance.methods.totalSupply().call()



  minted.innerText = totalSupply + "/" +maxSupply +" Mini Monkeys Adopted."



}



updatePage()



function updateValue(){

  console.log("updateValue")

  let target = document.querySelector('#count')

  if(parseInt(target.value) < 1){

    document.querySelector('#count').value = 1

  }
  if(parseInt(target.value) > 10){

    document.querySelector('#count').value = 10

  }

}



async function mint(){

  console.log("minting")



  let mintFee = await simpleMarketplace_instance.methods.mintFee().call()



  let target = document.querySelector('#count')

  let count = 1

  count = parseInt(target.value)

  count = count.toString()

  var price = mintFee * count



  hexNativeFees = window.web3.utils.toHex(price)



  var accounts = window.web3.eth.getAccounts().then(function(acc){

      parameter = {

          value: hexNativeFees,

          from: acc[0],

          gas: web3.utils.toHex(count*mintingGas),

          gasPrice: web3.utils.toHex(gasPrice)

      }



      simpleMarketplace_instance.methods.mint(count).send(parameter, (err, transactionHash) => {

          window.alert("Transaction sent: "+transactionHash)

          if(transactionHash){

          $('main').append('<div id="divLoading" style="margin: 0px; padding: 0px; position: fixed; right: 0px; top: 0px; width: 100%; height: 100%; background-color: rgb(102, 102, 102); z-index: 30001; opacity: 0.8;">\
            <p style="position: absolute; color: White; top: 50%; left: 45%;">\
            Pending transactions, please wait...\
            <img src="static/assets/create/loader.gif">\
            </p>\
            </div>');

          }

          tx_hash = transactionHash

      }).on('confirmation', () => {}).then((newContractInstance) => {

        setTimeout(removeLoader, 2000);

          window.alert('Minted')

      })

      .catch(function(error){

        setTimeout(removeLoader, 2000);

        window.alert("Minting failed")

      })

    })



}


