import { NgModule } from '@angular/core';
// import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';

import { HeroesComponent } from './heroes/heroes.component';

const routes: Routes = [
    { path: 'heroes',
      component: HeroesComponent }
];

@NgModule({
    imports: [
      // CommonModule
        RouterModule.forRoot(routes)
    ],
    // declarations: []
    exports: [ RouterModule ]
})
export class AppRoutingModule { }
