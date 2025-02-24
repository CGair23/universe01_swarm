from typing import (
    Callable,
)

from eth_typing import (
    ChecksumAddress,
)

from tree_graph.contract.web3._utils.rpc_abi import (
    RPC,
)
from tree_graph.contract.web3.method import (
    DeprecatedMethod,
    Method,
    default_root_munger,
)
from tree_graph.contract.web3.types import (
    BlockNumber,
    Wei,
)

make_dag: Method[Callable[[BlockNumber], bool]] = Method(
    RPC.miner_makeDag,
    mungers=[default_root_munger],
)


set_extra: Method[Callable[[str], bool]] = Method(
    RPC.miner_setExtra,
    mungers=[default_root_munger],
)


set_etherbase: Method[Callable[[ChecksumAddress], bool]] = Method(
    RPC.miner_setEtherbase,
    mungers=[default_root_munger],
)


set_gas_price: Method[Callable[[Wei], bool]] = Method(
    RPC.miner_setGasPrice,
    mungers=[default_root_munger],
)


start: Method[Callable[[int], bool]] = Method(
    RPC.miner_start,
    mungers=[default_root_munger],
)


stop: Method[Callable[[], bool]] = Method(
    RPC.miner_stop,
    mungers=None,
)


start_auto_dag: Method[Callable[[], bool]] = Method(
    RPC.miner_startAutoDag,
    mungers=None,
)


stop_auto_dag: Method[Callable[[], bool]] = Method(
    RPC.miner_stopAutoDag,
    mungers=None,
)


#
# Deprecated Methods
#
makeDag = DeprecatedMethod(make_dag, 'makeDag', 'make_dag')
setExtra = DeprecatedMethod(set_extra, 'setExtra', 'set_extra')
setEtherbase = DeprecatedMethod(set_etherbase, 'setEtherbase', 'set_etherbase')
setGasPrice = DeprecatedMethod(set_gas_price, 'setGasPrice', 'set_gas_price')
startAutoDag = DeprecatedMethod(start_auto_dag, 'startAutoDag', 'start_auto_dag')
stopAutoDag = DeprecatedMethod(stop_auto_dag, 'stopAutoDag', 'stop_auto_dag')
