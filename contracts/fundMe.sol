// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    // uint256 decimal = 10**18;
    //with mapping, we can't loop through it.
    mapping(address => uint256) public addressToAmountFunded;
    //so use another structure to store all address, and then use that to loop
    // all address in mapping.
    address[] public funders;
    address public owner;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    function fund() public payable {
        // uint256 minimumUSD = 50*decimal;
        uint256 minimumUSD = 50 * 1000000000000000000;

        require(
            getConvertRate(msg.value) >= minimumUSD,
            "THUAN contract require more ETH"
        );
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
        //you need the rate to covert from ETH-> USD by convert Rate!!!
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    //return eth price with 18 decimals behind-> actual return wei value dollar!
    function getPrice() public view returns (uint256) {
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        //answer actual return value of ETH with 8decimal behind! -> so i have to multi with 10 decimal too.
        return uint256(answer * 10000000000); //*1000000000 or 10000000000 (right seem better!) 10 zero numbers
        //should return around: 374431181187 -> convert 8 decimals-> 3,744.31181187 $
    }

    //wei = smallest value of eth number.
    //1 gwei = 1000000000 wei
    //convert value they send to us dollar
    //@param: ethAmount- wei value!
    //@return: also wei value!
    function getConvertRate(uint256 ehtAmount) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 real_value = (ethPrice * ehtAmount) / 1000000000000000000;
        return real_value;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public payable onlyOwner {
        //time to withdraw all money
        payable(msg.sender).transfer(address(this).balance);
        //set all other funders turn  to 0
        for (uint256 i; i < funders.length; i++) {
            address funder = funders[i];
            addressToAmountFunded[funder] = 0;
        }
        //re-construct all funders.
        funders = new address[](0);
    }
}
