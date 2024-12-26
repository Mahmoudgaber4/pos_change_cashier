/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { SelectionPopup } from "@point_of_sale/app/utils/input_popups/selection_popup";


class PosCashier extends Component {
static template = 'pos_change_cashier.PosCashier';

    setup() {
            this.pos = usePos();
            this.ui = useState(useService("ui"));
            this.popup = useService("popup");
        }

    async onClick() {
        console.log(this.pos)
        const users = this.pos.employees;

        const { confirmed, payload: selectedUser } = await this.popup.add(SelectionPopup, {
            title: ('Select a Cashier'),
            list: users.map(user => ({
                id: user.id,
                label: user.name,
                item: user,
            })),
        });

        if (confirmed) {
            this.pos.set_cashier(selectedUser);
        }
    }

}
ProductScreen.addControlButton({
    component: PosCashier,
    condition: () => true
})