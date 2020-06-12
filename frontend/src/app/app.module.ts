import { BrowserModule } from "@angular/platform-browser";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { NgModule } from "@angular/core";

import { HttpClientModule } from "@angular/common/http";
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { HomeComponent } from "./home/home.component";
import { LoginPageComponent } from "./login-page/login-page.component";
import { ChartModule, HIGHCHARTS_MODULES } from "angular-highcharts";
import { MainChartComponent } from "./home/main-chart/main-chart.component";
import { InfoCardComponent } from "./home/info-card/info-card.component";
import { GensetDetailComponent } from "./home/genset-detail/genset-detail.component";
import { ItemChartComponent } from "./home/genset-detail/item-chart/item-chart.component";
import { GensetMapsComponent } from './home/genset-maps/genset-maps.component';
import { ItemStockChartComponent } from './home/genset-detail/item-stock-chart/item-stock-chart.component';
import { ItemMapsComponent } from './home/genset-detail/item-maps/item-maps.component'
import stock from 'highcharts/modules/stock.src';
import more from 'highcharts/highcharts-more.src';
import { MainStockChartComponent } from './home/main-stock-chart/main-stock-chart.component';
import { NgxSpinnerModule } from "ngx-spinner";
import { NwbAllModule }  from '@wizishop/ng-wizi-bulma';
import { OwlDateTimeModule, OwlNativeDateTimeModule } from 'ng-pick-datetime';
import { TemperatureAlertComponent } from './temperature-alert/temperature-alert.component';
import { DataFeedComponent } from './home/data-feed/data-feed.component';
import { AddUserComponent } from './add-user/add-user.component';
import { LogoutPageComponent } from './logout-page/logout-page.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';



export function highchartsModules() {
  return [stock, more];
}

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    MainChartComponent,
    LoginPageComponent,
    InfoCardComponent,
    GensetDetailComponent,
    ItemChartComponent,
    GensetMapsComponent,
    ItemStockChartComponent,
    ItemMapsComponent,
    MainStockChartComponent,
    TemperatureAlertComponent,
    DataFeedComponent,
    AddUserComponent,
    LogoutPageComponent,
    NavBarComponent

  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    ChartModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    NgxSpinnerModule,
    NwbAllModule,
    OwlDateTimeModule,
    OwlNativeDateTimeModule,
  ],
  providers: [
    {provide: HIGHCHARTS_MODULES, useFactory: highchartsModules }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
