import { NgModule, Component } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { HomeComponent } from "./home/home.component";
import { LoginPageComponent } from "./login-page/login-page.component";
import { LogoutPageComponent } from "./logout-page/logout-page.component";
import { GensetDetailComponent } from "./home/genset-detail/genset-detail.component";
import { GensetMapsComponent } from "./home/genset-maps/genset-maps.component";
import { AddUserComponent } from "./add-user/add-user.component";



const routes: Routes = [
  { path: "", component: LoginPageComponent },
  { path: "logout", component: LogoutPageComponent },
  { path: "login", component: LoginPageComponent },
  { path: "home", component: HomeComponent },
  { path: "details/:id", component: GensetDetailComponent },
  { path: "maps", component: GensetMapsComponent },
  { path: "add_users", component: AddUserComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
