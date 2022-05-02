"""Initialization routines for ODE filters.

You may use the following (rough) guidelines to choose a suitable strategy
for low(ish) dimensional ODEs.

* ``num_derivatives = 1``: :class:`Stack`
* ``num_derivatives = 2``: :class:`StackWithJacobian` if a Jacobian is available,
  or :class:`NonProbabilisticFit` if not.
  If Jax is available, compute the Jacobian and use :class:`StackWithJacobian`,
  (or choose :class:`ForwardModeJVP` altogether).
* ``num_derivatives = 3,4,5``: :class:`NonProbabilisticFitWithJacobian`
  if the Jacobian of the ODE vector field is available,
  or :class:`NonProbabilisticFit` if not.
* ``num_derivatives > 5``: :class:`TaylorMode`. For orders 6 and 7,
  :class:`ForwardModeJVP` might work well too. :class:`TaylorMode` shines for
  ``num_derivatives >> 5``.

Initialization routines for high-dimensional ODEs are not implemented efficiently yet.

It may also be worth noting:

* Only automatic-differentiation-based routines yield the exact initialization.
  This becomes more desirable, the larger the number of modelled derivatives is.
* :class:`ForwardModeJVP` is generally more efficient than :class:`ForwardMode`. The
  jury is still out on the efficiency of :class:`ReverseMode`.
* :class:`Stack` and :class:`StackWithJacobian` are the only routines that come
  essentially for free.
  The other routines rely on either inference or automatic differentiation.
* For stiff ODEs, prefer :class:`NonProbabilisticFitWithJacobian` with ``BDF`` or
  ``Radau`` over :class:`NonProbabilisticFit` (or use one of the
  automatic-differentiation-based routines).
* Initialization routines can be chained together. For example, build a
  ``prior_process`` with an ``initrv`` that is generated by :class:`StackWithJacobian`,
  and initialize the ODE filter with :class:`NonProbabilisticFitWithJacobian`.
"""

from ._autodiff import ForwardMode, ForwardModeJVP, ReverseMode, TaylorMode
from ._interface import InitializationRoutine
from ._non_probabilistic_fit import NonProbabilisticFit, NonProbabilisticFitWithJacobian
from ._stack import Stack, StackWithJacobian

__all__ = [
    "InitializationRoutine",
    "Stack",
    "StackWithJacobian",
    "NonProbabilisticFit",
    "NonProbabilisticFitWithJacobian",
    "ForwardMode",
    "ForwardModeJVP",
    "ReverseMode",
    "TaylorMode",
]